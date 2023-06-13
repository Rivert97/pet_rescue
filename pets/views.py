from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PetSerializer, RecordSerializer
from .models import Pet, Record

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class PetViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows pets to be viewed or edited.
	"""
	queryset = Pet.objects.all()
	serializer_class = PetSerializer
	permission_classes = [permissions.IsAuthenticated]

class RecordViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows registers to be viewed or edited.
	"""
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
	permission_classes = [permissions.IsAuthenticated]
