from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from .validations import validate_register_data
from .serializers import RegisterSerializer

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
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)