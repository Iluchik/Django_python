from django.contrib.auth.models import User
from django.db import models
from main.models import Lesson
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	group = models.CharField(max_length=250)
	about = models.TextField()
	verified_lessons = models.ManyToManyField(Lesson)