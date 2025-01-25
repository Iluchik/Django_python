from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime, timedelta, date

class Category(models.Model):
	name = CharField(max_length=1000, unique=True)

	def __str__(self):
		return self.name

class stud_on_lesson(models.Model):
	user_id = models.IntegerField()

	def __str__(self) -> str:
		return self.user_id

class Lesson(models.Model):
	title = models.CharField(max_length=250)
	lecturer = models.CharField(max_length=250)
	group = models.CharField(max_length=250)
	start_time = models.TimeField()
	classroom = models.CharField(max_length=250)
	date = models.DateField()
	file = models.FileField(upload_to="lessons/", blank=True) # optional
	slug = models.SlugField(max_length=1000, unique=True)
	category = models.OneToOneField(Category, related_name="categories", on_delete=models.CASCADE, default=1)
	verification_code = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		if not self.slug and not self.id:
			self.slug = slugify(self.title)
		super(Lesson, self).save(*args, **kwargs)

	def get_end_time(self):
		return (datetime.combine(date(1,1,1), self.start_time) + timedelta(hours=1, minutes=30)).time()

	def __str__(self):
		return f"{self.date}T{self.start_time} | {self.title} | {self.category}"