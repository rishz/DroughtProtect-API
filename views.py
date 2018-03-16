from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import JWTSerializer

class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer