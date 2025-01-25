from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
	path("", views.index, name="home"),
	re_path(r"^lesson/(?P<id>[0-9]+)/(?P<group>М([1-9]|1[0-2]|14)О-[1-6]([1-9][0-9]|[0-9][1-9])(Б|Бки|БВ|М|Мки|СВ|С|А)-(1[8-9]|2[0-4]))/$", views.attendance, name="lesson"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)