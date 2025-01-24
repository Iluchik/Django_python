from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

def register_view(req):
	if req.method == "POST":
		form = RegistrationForm(req.POST)
		profile_form = ProfileInfoForm(req.POST)
		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			students, created = Group.objects.get_or_create(name="students")
			students.user_set.add(user)
			print("save")
			return redirect("login")
		else:
			error = form.errors
			print(error)
	form = RegistrationForm()
	profile_form = ProfileInfoForm()
	context = {"form": form, "profile_form": profile_form}
	return render(req, "users/registration.html", context)

def login_view(req):
	if req.method == "POST":
		form = LoginForm(req.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				login(req, user)
				return redirect("profile")
	form = LoginForm()
	return render(req, "users/login.html", context={"form":form})

def logout_view(req):
	logout(req)
	return redirect("/")

def profile(req):
	if req.user.is_authenticated:
		return render(req, "users/profile.html")
	else:
		return redirect("login")