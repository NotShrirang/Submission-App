# Generated by Django 4.1.7 on 2023-06-30 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submission",
            old_name="hackthon",
            new_name="hackathon",
        ),
    ]