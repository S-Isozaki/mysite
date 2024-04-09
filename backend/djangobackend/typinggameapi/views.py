from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from django.http import JsonResponse

from .validations import validate_register_data, validate_signin_data
from .serializers import RegisterSerializer, SigninSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return JsonResponse(data={"msg": "pass"}, status=200)

class Register(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        try:
            clean_data = validate_register_data(request.data)
            serializer = RegisterSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response(data={"error": ve.message}, status=status.HTTP_400_BAD_REQUEST)

class Signin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        clean_data = validate_signin_data(request.data)
        serializer = SigninSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(clean_data)
        if user:
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class Signout(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)