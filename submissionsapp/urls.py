from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .app.views import HackathonView, SubmissionView, UserView, UserCreateView, RegisterView, HackathonEnrolledView, HackathonSubmissionsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'hackathons', HackathonView)
router.register(r'submissions', SubmissionView)
router.register(r'users', UserView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/users/create/', UserCreateView.as_view(), name='create_user'),
    path('api/hackathons/<str:hackathon_id>/register/', RegisterView.as_view(), name='register'),
    path('api/<str:user_id>/hackathons/', HackathonEnrolledView.as_view(), name='user_hackathons'),
    path('api/<str:user_id>/hackathons/<str:hackathon_id>/submissions/', HackathonSubmissionsView.as_view(), name='user_hackathon_submissions'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
