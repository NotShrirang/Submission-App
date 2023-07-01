from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .app.views import HackathonView, SubmissionView, UserView

router = routers.DefaultRouter()
router.register(r'hackathons', HackathonView)
router.register(r'submissions', SubmissionView)
router.register(r'users', UserView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
