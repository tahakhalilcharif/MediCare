from django.db import models

class Patient(models.Model):
    Patient_ID = models.AutoField(primary_key=True)
    NSS = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField()

class Doctor(models.Model):
    Doctor_ID = models.AutoField(primary_key=True)
    NSS = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Specialisation = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField()

class Visit(models.Model):
    Visit_ID = models.AutoField(primary_key=True)
    Consultation_Date = models.DateField(blank=True, null=True)
    Appointment_Date = models.DateField(blank=True, null=True)
    Visit_Time = models.TimeField(blank = True )
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    treatment_plan = models.ForeignKey('TreatmentPlan', on_delete=models.CASCADE , default=0)

class MedicalRecord(models.Model):
    Record_ID = models.AutoField(primary_key=True)
    Patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

class TreatmentPlan(models.Model):
    Plan_ID = models.AutoField(primary_key=True)
    Diagnosis = models.TextField()
    Treatment_Details = models.TextField()
    Medical_Record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)

class Prescription(models.Model):
    Prescription_ID = models.AutoField(primary_key=True)
    Medication = models.CharField(max_length=255)
    Dose = models.CharField(max_length=255)
    Serial_Number = models.CharField(max_length=255)
    Treatment_Plan = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE)
    Prescription_Date = models.DateField()