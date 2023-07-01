from django.db import models
from django.contrib.auth.models import User

class Hackathon(models.Model):

    SUBMISSION_TYPE_CHOICES = (
        ('image', 'image'),
        ('file', 'file'),
        ('link', 'link'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.FileField(upload_to='images/')
    hackathon_image = models.FileField(upload_to='images/')
    submission_type = models.CharField(max_length=5, choices=SUBMISSION_TYPE_CHOICES)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(auto_now=True)
    reward_prize = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    submission_file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return self.name
