from django.shortcuts import render, get_object_or_404 #because of this line we can reder direcect to template without using hhttp
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin#redirect to the login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
#from django.http import HttpResponse

def home(request):
	#return HttpResponse('<h1>Blog Home </h1>')
# Create your views here.
	context = {

	'posts' : Post.objects.all()
	}
	return render(request,'blog/home.html',context )

class PostListView(ListView): #generic display
	model = Post
	template_name = 'blog/home.html'
	context_object_name ='posts'
	ordering = ['-date_posted']
	paginate_by = 2

class UserPostListView(ListView): #generic display
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name ='posts'
	ordering = ['-date_posted']
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView): #generic display
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #generic display
	model = Post
	fields = ['title', 'content']
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): #generic display
	model = Post
	fields = ['title', 'content']
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
#prevent othher user from update thhe post 
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView): #generic display
	model = Post
	success_url ='/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	#return HttpResponse('<h1>Blog About </h1>')
	context = {

	'posts' : Post.objects.all()
	}
	return render(request,'blog/about.html', {'title': 'About'})
	
def mainPage(request):
	return render(request,'blog/index.html')