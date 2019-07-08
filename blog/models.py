from django.db import models
from django.utils import timezone #take consideration of our timezone
from django.contrib.auth.models import User  #to make model have a relationship User
from django.urls import reverse
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default= timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	#auto_now_add=True update the time when the object is created, cannot chhanged the date after created-> so it's better to use default
	#on_delete = models.CASCADE : if user is deleted, delete the post as well
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
