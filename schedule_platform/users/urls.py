from django.urls import path
from . import views

urlpatterns = [
	path("registration", views.register_view, name="registration"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("profile", views.profile, name="profile")
]