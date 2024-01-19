from django import forms
from .models import *

#Doctor Forms
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class AddDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ('Doctor_ID',)

class UpdateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class TreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = '__all__'

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['Patient_ID'] 

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class AddVisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['Visit_ID'] 

class UpdateVisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

class AddMedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        exclude = ['Record_ID'] 

class UpdateMedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class AddTreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        exclude = ['Plan_ID'] 

class UpdateTreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = '__all__'

class AddPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = ['Prescription_ID']

class UpdatePrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
