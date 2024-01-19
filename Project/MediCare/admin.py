from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(TreatmentPlan)
admin.site.register(Prescription)
admin.site.register(Visit)
