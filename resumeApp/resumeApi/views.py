# api that helps to get and excess candidates resumes and profile images
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [BasicAuthentication ]
    permission_classes=[IsAuthenticated,DjangoModelPermissions]
    