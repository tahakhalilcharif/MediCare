from django.urls import path 
from . import views
from .views import *

urlpatterns = [

    #Doctors
    path('doctors/', doctor_list, name='doctor_list'),
    path('add-doctor/', add_doctor, name='add_doctor'),
    path('update-doctor/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('delete-doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),

    # Patients
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:patient_id>/update/', views.update_patient, name='update_patient'),
    path('patients/<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),
    path('patients/<int:patient_id>/medical-record/', views.patient_medical_record, name='patient_medical_record'),
    
    # Visits
    path('visits/', views.visit_list, name='visit_list'),
    path('visits/add/', views.add_visit, name='add_visit'),
    path('visits/<int:visit_id>/', views.visit_detail, name='visit_detail'),
    path('visits/<int:visit_id>/update/', views.update_visit, name='update_visit'),
    path('visits/<int:visit_id>/delete/', views.delete_visit, name='delete_visit'),

    # Medical Records
    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    path('medical-records/add/', views.add_medical_record, name='add_medical_record'),
    path('medical-records/<int:medical_record_id>/', views.medical_record_detail, name='medical_record_detail'),
    path('medical-records/<int:medical_record_id>/update/', views.update_medical_record, name='update_medical_record'),
    path('medical-records/<int:medical_record_id>/delete/', views.delete_medical_record, name='delete_medical_record'),

    # Treatment Plans
    path('treatment-plans/', views.treatment_plan_list, name='treatment_plan_list'),
    path('treatment-plans/add/', views.add_treatment_plan, name='add_treatment_plan'),
    path('treatment-plans/<int:treatment_plan_id>/', views.treatment_plan_detail, name='treatment_plan_detail'),
    path('treatment-plans/<int:treatment_plan_id>/update/', views.update_treatment_plan, name='update_treatment_plan'),
    path('treatment-plans/<int:treatment_plan_id>/delete/', views.delete_treatment_plan, name='delete_treatment_plan'),

    # Prescriptions
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/add/', views.add_prescription, name='add_prescription'),
    path('prescriptions/<int:prescription_id>/', views.prescription_detail, name='prescription_detail'),
    path('prescriptions/<int:prescription_id>/update/', views.update_prescription, name='update_prescription'),
    path('prescriptions/<int:prescription_id>/delete/', views.delete_prescription, name='delete_prescription'),
]