from .models import Pet, Record, RecordLog
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'email']

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pet
		fields = ['owner', 'id', 'animal', 'name', 'description']
		read_only_fields = ['owner']

class RecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Record
		fields = ['responsible', 'pet', 'description', 'lost_location', 'status']
