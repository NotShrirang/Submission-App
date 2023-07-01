from .models import Hackathon, Submission
from rest_framework import serializers
from django.contrib.auth.models import User

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['id', 'title', 'description', 'background_image', 'hackathon_image', 'submission_type', 'start_datetime', 'end_datetime', 'reward_prize', 'registered_users']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'hackathon', 'user', 'name', 'summary', 'summary', 'submission_file']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email",
                  "is_staff", "is_active", "date_joined", "last_login"]