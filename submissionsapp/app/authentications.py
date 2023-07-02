from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthenticationOnlyForAPI(JWTAuthentication):
    def authenticate(self, request):
        if request.path.startswith('/api/'):
            return super().authenticate(request)
        return None