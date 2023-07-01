from rest_framework import viewsets
from .models import Hackathon, Submission
from .serializers import HackathonSerializer, SubmissionSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from django.contrib.auth.models import User

class HackathonView(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    def list(self, request):
        return super().list(request)
    
    def retrieve(self, request, pk=None):
        queryset = Hackathon.objects.get(id=pk)
        serializer = HackathonSerializer(queryset)
        return JsonResponse(serializer.data)
    
    def create(self, request):
        jsonData = dict(request.data)
        for key, value in jsonData.items():
            jsonData[key] = value[0]
        print(jsonData)
        serializer = HackathonSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    
    def update(self, request, pk=None):
        return super().update(request, pk)
    
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)
    
    def destroy(self, request, pk=None):
        super().destroy(request, pk)
        return JsonResponse({"message": "Hackathon deleted successfully!"})

class SubmissionView(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def list(self, request):
        return super().list(request)
    
    def retrieve(self, request, pk=None):
        queryset = Submission.objects.get(id=pk)
        serializer = SubmissionSerializer(queryset)
        return JsonResponse(serializer.data)
    
    def create(self, request):
        jsonData = dict(request.data)
        for key, value in jsonData.items():
            jsonData[key] = value[0]
        serializer = SubmissionSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    
    def update(self, request, pk=None):
        return super().update(request, pk)
    
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)
    
    def destroy(self, request, pk=None):
        super().destroy(request, pk)
        return JsonResponse({"message": "Submission deleted successfully!"})

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        return super().list(request)
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.get(id=pk)
        serializer = UserSerializer(queryset)
        return JsonResponse(serializer.data)
    
    def create(self, request):
        jsonData = JSONParser().parse(request)
        serializer = UserSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    
    def update(self, request, pk=None):
        return super().update(request, pk)
    
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)
    
    def destroy(self, request, pk=None):
        return super().destroy(request, pk)