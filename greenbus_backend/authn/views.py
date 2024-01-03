from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .serializers import UserSignupSerializer, UserProfileSerializer

@api_view(['POST'])
@authentication_classes([])
@permission_classes((AllowAny,))
def user_signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user_profile = UserProfile.objects.create(user=user, user_type='user')
        login(request, user)

        user_profile_serializer = UserProfileSerializer(user_profile)
        return Response(user_profile_serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([])
@permission_classes((AllowAny,))
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
