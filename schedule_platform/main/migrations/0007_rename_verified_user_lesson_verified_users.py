# Generated by Django 5.1.4 on 2025-01-25 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_lesson_verified_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lesson",
            old_name="verified_user",
            new_name="verified_users",
        ),
    ]
