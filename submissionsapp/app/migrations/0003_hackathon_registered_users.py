# Generated by Django 4.2.2 on 2023-07-01 16:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0002_rename_hackthon_submission_hackathon"),
    ]

    operations = [
        migrations.AddField(
            model_name="hackathon",
            name="registered_users",
            field=models.ManyToManyField(
                blank=True, default=[], null=True, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]