# Generated by Django 5.0.7 on 2024-09-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parent", "0003_remove_student_password_remove_student_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="password",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="username",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]