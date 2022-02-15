from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', PatientsList.as_view(), name='home'),

    path('add_patient/<int:face>/', AddPatient.as_view(), name='add_patient'),
    path('patient_card/<int:pk>/', PatientCard.as_view(), name='patient_card'),
    path('patients_list/', PatientsList.as_view(), name='patients_list'),

    path('doctors_list/', DoctorsList.as_view(), name='doctors_list'),

    path('add_staff_face/', AddFace.as_view(), name='add_staff_face'),
    path('add_patient_face/', AddFace.as_view(), name='add_patient_face'),
    path('face_card/<int:pk>/', FaceCard.as_view(), name='face_card'),
    path('faces_list/', FacesList.as_view(), name='faces_list'),

    path('add_staff/<int:face>/', AddStaff.as_view(), name='add_staff'),
    path('staff_card/<int:pk>/', StaffCard.as_view(), name='staff_card'),
    path('staff_list/', StaffList.as_view(), name='staff_list'),

    path('add_visit/', AddVisit.as_view(), name='add_visit'),
    path('visit_card/<int:pk>/', VisitCard.as_view(), name='visit_card'),
    path('patient_visits_list/<int:patient>/', VisitList.as_view(), name='patient_visits_list'),
    path('doctor_visits_list/<int:doctor>/', VisitList.as_view(), name='doctor_visits_list'),
]
