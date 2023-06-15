from .models import Pet, Record, RecordLog
from rest_framework import serializers

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pet
		fields = ['owner', 'id', 'animal', 'name', 'description']
		read_only_fields = ['owner']

class RecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Record
		fields = ['id', 'responsible', 'pet', 'description', 'lost_location', 'status']
		read_only_fields = ['id', 'responsible']
	
	def validate(self, data):
		# Validamos la mascota
		pet = Pet.objects.filter(id=data['pet'].id, owner=self.context['request'].user.id)
		if not pet:
			raise serializers.ValidationError({'pet': "Pet doesn't belong to the current user"})
		return data

class RecordLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = RecordLog
		fields = ['user', 'record', 'description', 'seen_location', 'picked_up', 'created_at']
		read_only_fields = ['user', 'record', 'created_at']
