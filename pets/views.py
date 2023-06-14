from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Pet, Record
from .serializers import UserSerializer, PetSerializer, RecordSerializer

class UserList(generics.ListCreateAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserSerializer

	def destroy(self, request, *args, **kwargs):
		user = self.get_object()
		user.is_active = False
		user.save()
		return Response(data={'detail': 'Success'})
	
class PetList(generics.ListCreateAPIView):
	"""
	API endpoint that allows pets to be viewed or edited.
	"""
	queryset = Pet.objects.filter(is_active=True)
	serializer_class = PetSerializer

	def list(self, request, *args, **kwargs):
		pets = self.get_queryset().filter(owner=request.user)
		serializer = PetSerializer(pets, many=True)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = PetSerializer(data=request.data)
		if serializer.is_valid():
			pet = serializer.save(owner=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_CREATED)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pet.objects.filter(is_active=True)
	serializer_class = PetSerializer

	def get_object(self):
		if self.request.method == 'GET':
			return super().get_object()
		else:
			queryset = self.get_queryset()
			obj = get_object_or_404(queryset, owner=self.request.user, **self.kwargs)
			return obj

	def destroy(self, request, *args, **kwargs):
		pet = self.get_object()
		pet.is_active = False
		pet.save()
		return Response(data={'detail': 'Success'})

