from django.contrib import admin
from .models import Pet, Record, RecordLog

# Register your models here.
admin.site.register(Pet)
admin.site.register(Record)
admin.site.register(RecordLog)
