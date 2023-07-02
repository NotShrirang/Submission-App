from rest_framework import views, viewsets
from rest_framework.permissions import IsAuthenticated
from .authentications import JWTAuthenticationOnlyForAPI
from .models import Hackathon, Submission
from .serializers import HackathonSerializer, SubmissionSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from django.contrib.auth.models import User
from datetime import datetime

class HackathonView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthenticationOnlyForAPI]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [JWTAuthenticationOnlyForAPI]
    permission_classes = [IsAuthenticated]
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
        IMAGES = ["image/png", "image/jpeg", "image/jpg"]
        hackathon_obj = Hackathon.objects.get(id=jsonData["hackathon"])
        hour = hackathon_obj.end_datetime.hour
        minute = hackathon_obj.end_datetime.minute
        second = hackathon_obj.end_datetime.second
        day = hackathon_obj.end_datetime.day
        month = hackathon_obj.end_datetime.month
        year = hackathon_obj.end_datetime.year
        datetime_obj = datetime(year, month, day, hour, minute, second)
        if datetime.now() > datetime_obj:
            return JsonResponse({"message": "Hackathon ended!"})
        if hackathon_obj.submission_type == "image" and jsonData["submission_file"].content_type not in IMAGES:
            return JsonResponse({"message": "Invalid file type. File type should be image!"})
        if hackathon_obj.submission_type == "file" and not jsonData["submission_file"].content_type.startswith("application"):
            return JsonResponse({"message": "Invalid file type."})
        if hackathon_obj.submission_type == "link" and not jsonData["submission_file"].startswith("http"):
            return JsonResponse({"message": "Invalid link!"})
        if not hackathon_obj.registered_users.filter(id=jsonData["user"]).exists():
            return JsonResponse({"message": "User is not registered for this hackathon!"})
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
    authentication_classes = [JWTAuthenticationOnlyForAPI]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        return super().list(request)
    
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    def create(self, request):
        return JsonResponse({"message": "POST method not allowed!"})
    
    def update(self, request, pk=None):
        return super().update(request, pk)
    
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)
    
    def destroy(self, request, pk=None):
        super().destroy(request, pk)
        return JsonResponse({"message": "User deleted successfully!"})


class UserCreateView(views.APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        jsonData = JSONParser().parse(request)
        serializer = UserSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

class RegisterView(views.APIView):
    parser_classes = [JSONParser]

    def post(self, request, hackathon_id):
        jsonData = JSONParser().parse(request)
        hackathon = Hackathon.objects.get(id=hackathon_id)
        hackathon.registered_users.add(jsonData["user_id"])
        hackathon.save()
        return JsonResponse({"message": "User registered successfully!"})
    
    def delete(self, request, hackathon_id):
        jsonData = JSONParser().parse(request)
        hackathon = Hackathon.objects.get(id=hackathon_id)
        hackathon.registered_users.remove(jsonData["user_id"])
        hackathon.save()
        return JsonResponse({"message": "User unregistered successfully!"})
    
class HackathonEnrolledView(views.APIView):
    parser_classes = [JSONParser]

    def get(self, request, user_id):
        hackathons = Hackathon.objects.filter(registered_users__in=user_id)
        serializer = HackathonSerializer(hackathons, many=True)
        return JsonResponse(serializer.data, safe=False)
    
class HackathonSubmissionsView(views.APIView):
    parser_classes = [JSONParser]

    def get(self, request, user_id, hackathon_id):
        submissions = Submission.objects.filter(hackathon=hackathon_id, user=user_id)
        serializer = SubmissionSerializer(submissions, many=True)
        return JsonResponse(serializer.data, safe=False)