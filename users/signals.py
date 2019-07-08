from django.db.models.signals import post_save #signal when object is created
from django.contrib.auth.models import User
from django.dispatch import receiver #get the signal and perform some tasks
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender= User)
def save_profile(sender,instance,created, **kwargs):
	instance.profile.save()

#xem lai concept cua signal ^ create profile when the user is created