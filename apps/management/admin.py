from django.contrib import admin
from .models import Doctor, Patient, User, Appointment, Accepted_Data

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Accepted_Data)
