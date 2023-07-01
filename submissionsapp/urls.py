from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .app.views import HackathonView, SubmissionView, UserView, RegisterView, HackathonEnrolledView, HackathonSubmissionsView

router = routers.DefaultRouter()
router.register(r'hackathons', HackathonView)
router.register(r'submissions', SubmissionView)
router.register(r'users', UserView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('hackathons/<str:hackathon_id>/register/', RegisterView.as_view(), name='register'),
    path('<str:user_id>/hackathons/', HackathonEnrolledView.as_view(), name='user_hackathons'),
    path('<str:user_id>/hackathons/<str:hackathon_id>/submissions/', HackathonSubmissionsView.as_view(), name='user_hackathon_submissions'),
]
