from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Pet, Record, RecordLog
from .serializers import PetSerializer, RecordSerializer, RecordLogSerializer

class PetList(generics.ListCreateAPIView):
	"""
	API endpoint that allows pets to be viewed or edited.
	"""
	queryset = Pet.objects.filter(is_active=True)
	serializer_class = PetSerializer
	permission_classes = [permissions.IsAuthenticated]

	def list(self, request):
		pets = self.get_queryset().filter(owner=request.user)
		serializer = PetSerializer(pets, many=True)
		return Response(serializer.data)

	def create(self, request):
		serializer = PetSerializer(data=request.data)
		if serializer.is_valid():
			pet = serializer.save(owner=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pet.objects.filter(is_active=True)
	serializer_class = PetSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_object(self):
		if self.request.method == 'GET':
			return super().get_object()
		else:
			queryset = self.get_queryset()
			obj = get_object_or_404(queryset, owner=self.request.user, **self.kwargs)
			return obj

	def destroy(self, request):
		pet = self.get_object()
		pet.is_active = False
		pet.save()
		return Response(data={'detail': 'Success'})

class RecordList(generics.ListCreateAPIView):
	"""
	API endpoint that allows records to be viewed.
	"""
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
	permission_classes = [permissions.IsAuthenticated]

	def create(self, request):
		serializer = RecordSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			record = serializer.save(responsible=request.user)
			# Creamos un evento
			recordlog = RecordLog(user=request.user, description="Se abre aviso")
			recordlog.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_object(self):
		if self.request.method == 'GET':
			return super().get_object()
		else:
			queryset = self.get_queryset()
			obj = get_object_or_404(queryset, responsible=self.request.user.id, **self.kwargs)
			return obj

	def destroy(self, request):
		record = self.get_object()
		record.status = "D"
		record.save()
		return Response(data={'detail': 'Success'})

class RecordLogList(generics.ListCreateAPIView):
	"""
	API endpoint that allows records logs to be viewed.
	"""
	queryset = RecordLog.objects.all()
	serializer_class = RecordLogSerializer
	permission_classes = [permissions.IsAuthenticated]

	def list(self, request, record_pk):
		logs = self.get_queryset().filter(record=record_pk)
		serializer = RecordLogSerializer(logs, many=True)
		return Response(serializer.data)

	def create(self, request, record_pk):
		serializer = RecordLogSerializer(data=request.data)
		if serializer.is_valid():
			record = Record.objects.get(id=record_pk)
			recordlog = serializer.save(user=request.user, record=record)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

