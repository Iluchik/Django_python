# Generated by Django 5.1.4 on 2025-01-04 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_category_name_remove_lesson_categories_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lesson",
            old_name="time",
            new_name="start_time",
        ),
    ]
