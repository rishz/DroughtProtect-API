import jwt,json
from rest_framework import views, status, exceptions
from django.http import HttpResponse
from rest_framework.response import Response
from auth.models import User
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([])
@permission_classes([])
class Login(views.APIView):

    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400")

        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email)
            user.check_password(password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid email/password"}, status="400")

        if user:
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
                json.dumps(jwt_token),
                status=200,
                content_type="application/json"
            )
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )

@authentication_classes([])
@permission_classes([])
class Register(views.APIView):

    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400")

        email = request.data['email']
        password = request.data['password']

        if User.objects.filter(email=email).exists():
            return Response(
                {'Error': "User already exists"},
                status="400"
            )

        user = User(email=email)
        user.set_password(password)
        user.save()

        return HttpResponse(
            json.dumps({'Status': "Ok"}),
            status=200,
            content_type="application/json"
        )

class Verify_Token(views.APIView):

    def get(self, request, *args, **kwargs):

        return HttpResponse(
            json.dumps({'Status': "Ok"}),
            status=200,
            content_type="application/json"
        )