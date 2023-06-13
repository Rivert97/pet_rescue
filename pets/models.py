from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
	ANIMALS = [
		("D", "Dog"),
		("C", "Cat"),
	]
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	animal = models.CharField(max_length=1, choices=ANIMALS, default="D")
	name = models.CharField(max_length=60, default="")
	description = models.CharField(max_length=255, default="")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Record(models.Model):
	STATUS = [
		("A", "Active"),
		("I", "Inactive"),
		("E", "Ended"),
		("D", "Deleted"),
	]
	responsible = models.ForeignKey(User, on_delete=models.CASCADE)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	description = models.CharField(max_length=255, default="")
	lost_location = models.CharField(max_length=255, default="")
	status = models.CharField(max_length=1, choices=STATUS, default="A")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class RecordLog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=255, default="")
	seen_location = models.CharField(max_length=255, default="", blank=True)
	picked_up = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

