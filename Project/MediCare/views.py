from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

#Doctor View For Admin Only
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    return render(request, 'doctor_detail.html', {'form': form, 'doctor': doctor})

def add_doctor(request):
    if request.method == 'POST':
        form = AddDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = AddDoctorForm()

    return render(request, 'add_doctor.html', {'form': form})

def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    form = UpdateDoctorForm(instance=doctor)

    if request.method == 'POST':
        form = UpdateDoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    return render(request, 'update_doctor.html', {'form': form, 'doctor': doctor})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    doctor.delete()
    return redirect('doctor_list')


#Patient view accesible by doctors , admin and receptionist 
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')

    return render(request, 'patient_detail.html', {'form': form, 'patient': patient})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})

def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')

    return render(request, 'update_patient.html', {'form': form, 'patient': patient})

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    patient.delete()
    return redirect('patient_list')


#View for visits accesible by admin and receptionst
def visit_list(request):
    visits = Visit.objects.all()
    return render(request, 'visit_list.html', {'visits': visits})

def visit_detail(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    form = VisitForm(instance=visit)

    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_list')

    return render(request, 'visit_detail.html', {'form': form, 'visit': visit})

def add_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm()

    return render(request, 'add_visit.html', {'form': form})

def update_visit(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    form = VisitForm(instance=visit)

    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_list')

    return render(request, 'update_visit.html', {'form': form, 'visit': visit})

def delete_visit(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    visit.delete()
    return redirect('visit_list')


#Medical records view accesible by admin and doctors
def medical_record_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'medical_record_list.html', {'medical_records': medical_records})

def medical_record_detail(request, medical_record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=medical_record_id)
    form = MedicalRecordForm(instance=medical_record)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')

    return render(request, 'medical_record_detail.html', {'form': form, 'medical_record': medical_record})

def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm()

    return render(request, 'add_medical_record.html', {'form': form})

def update_medical_record(request, medical_record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=medical_record_id)
    form = MedicalRecordForm(instance=medical_record)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')

    return render(request, 'update_medical_record.html', {'form': form, 'medical_record': medical_record})

def delete_medical_record(request, medical_record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=medical_record_id)
    medical_record.delete()
    return redirect('medical_record_list')


#Treatment plan view accesible by admin and doctors
def treatment_plan_list(request):
    treatment_plans = TreatmentPlan.objects.all()
    return render(request, 'treatment_plan_list.html', {'treatment_plans': treatment_plans})

def treatment_plan_detail(request, treatment_plan_id):
    treatment_plan = get_object_or_404(TreatmentPlan, pk=treatment_plan_id)
    form = TreatmentPlanForm(instance=treatment_plan)

    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST, instance=treatment_plan)
        if form.is_valid():
            form.save()
            return redirect('treatment_plan_list')

    return render(request, 'treatment_plan_detail.html', {'form': form, 'treatment_plan': treatment_plan})

def add_treatment_plan(request):
    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treatment_plan_list')
    else:
        form = TreatmentPlanForm()

    return render(request, 'add_treatment_plan.html', {'form': form})

def update_treatment_plan(request, treatment_plan_id):
    treatment_plan = get_object_or_404(TreatmentPlan, pk=treatment_plan_id)
    form = TreatmentPlanForm(instance=treatment_plan)

    if request.method == 'POST':
        form = TreatmentPlanForm(request.POST, instance=treatment_plan)
        if form.is_valid():
            form.save()
            return redirect('treatment_plan_list')

    return render(request, 'update_treatment_plan.html', {'form': form, 'treatment_plan': treatment_plan})

def delete_treatment_plan(request, treatment_plan_id):
    treatment_plan = get_object_or_404(TreatmentPlan, pk=treatment_plan_id)
    treatment_plan.delete()
    return redirect('treatment_plan_list')

#Prescription View accesible by admin and doctors
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescription_list.html', {'prescriptions': prescriptions})

def prescription_detail(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    form = PrescriptionForm(instance=prescription)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')

    return render(request, 'prescription_detail.html', {'form': form, 'prescription': prescription})

def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()

    return render(request, 'add_prescription.html', {'form': form})

def update_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    form = PrescriptionForm(instance=prescription)

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')

    return render(request, 'update_prescription.html', {'form': form, 'prescription': prescription})

def delete_prescription(request, prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    prescription.delete()
    return redirect('prescription_list')

def patient_medical_record(request, patient_id):
    patient = get_object_or_404(Patient, Patient_ID=patient_id)
    medical_records = MedicalRecord.objects.filter(Patient=patient)
    
    for record in medical_records:
        record.treatment_plans = TreatmentPlan.objects.filter(Medical_Record=record)
        for plan in record.treatment_plans:
            plan.prescription = Prescription.objects.filter(Treatment_Plan=plan).first()
            plan.visit = Visit.objects.filter(Treatment_Plan=plan).first()

    context = {
        'patient': patient,
        'medical_records': medical_records,
    }

    return render(request, 'patient_medical_record.html', context)