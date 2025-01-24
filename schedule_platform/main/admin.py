from django.contrib import admin
from .models import *

class LessonAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Category)