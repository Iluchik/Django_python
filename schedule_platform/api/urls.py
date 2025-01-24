from django.urls import path
from . import views

urlpatterns = [
	path("category/", views.CategoryAPI.as_view(), name="categories_api")
]