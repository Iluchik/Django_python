from django.shortcuts import render
from .models import *

def index(req):
	categories = Category.objects.all()
	lessons = Lesson.objects.all()
	context = {
		"categories": categories,
		"lessons": lessons,
	}

	return render(req, "main/index.html", context=context)

def attendance(req):
	pass