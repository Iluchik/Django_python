from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from users.models import Profile
from .forms import VerificationForm
from random import randint

def index(req):
	categories = Category.objects.all()
	lessons = Lesson.objects.all()
	context = {
		"categories": categories,
		"lessons": lessons,
	}

	return render(req, "main/index.html", context=context)

def attendance(req, id, group):
	lesson = Lesson.objects.get(id=id)
	if req.method == "POST":
		form = VerificationForm(req.POST)
		if form.is_valid():
			code = form.cleaned_data["code"]
			if lesson.verification_code == int(code):
				req.user.profile.verified_lessons.add(lesson.id)
				print(f"added {req.user} to {lesson.title}")
				return redirect("/")
	form = VerificationForm()
	if lesson.verification_code == 0:
		lesson.verification_code = randint(1000000000, 1000000000000000)
		lesson.save()
	users = User.objects.all()
	verified_profiles = Profile.objects.filter(verified_lessons__title=lesson.title)
	verified_users = []
	for profile in verified_profiles:
		verified_user = User.objects.get(id=profile.user_id)
		verified_users.append(verified_user)
	context = {
		"form": form,
		"lesson": lesson,
		"users": users,
		"group": group,
		"verified_users": verified_users
	}

	return render(req, "main/attendance.html", context=context)