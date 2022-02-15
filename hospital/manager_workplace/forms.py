from django import forms
from .models import *


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['blood_type', 'hiv_status', 'height', 'weight', 'allergies', 'required_medical_policy',
                  'add_medical_policy', 'notes']
        widgets = {
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'hiv_status': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'required_medical_policy': forms.TextInput(attrs={'class': 'form-control'}),
            'add_medical_policy': forms.TextInput(attrs={'class': 'form-control'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FaceForm(forms.ModelForm):
    class Meta:
        model = Faces
        fields = ['surname', 'name', 'patronymic', 'gender', 'date_of_birth', 'doc_type', 'doc_series', 'doc_number',
                  'doc_date', 'doc_given', 'doc_code_division', 'snils', 'inn', 'registration', 'phone', 'email',
                  'notes']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'doc_type': forms.Select(attrs={'class': 'form-control'}),
            'doc_series': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_date': forms.DateInput(attrs={'class': 'form-control'}),
            'doc_given': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_code_division': forms.TextInput(attrs={'class': 'form-control'}),
            'snils': forms.TextInput(attrs={'class': 'form-control'}),
            'inn': forms.TextInput(attrs={'class': 'form-control'}),
            'registration': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visits
        fields = ['patient', 'doctor', 'date', 'time']


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['post', 'speciality', 'education_document', 'edu_doc_series', 'edu_doc_number',
                  'edu_doc_date', 'tab_number', 'salary', 'hire_date', 'fire_date']
        widgets = {
            'post': forms.Select(attrs={'class': 'form-control'}),
            'speciality': forms.Select(attrs={'class': 'form-control'}),
            'education_document': forms.Select(attrs={'class': 'form-control'}),
            'edu_doc_series': forms.TextInput(attrs={'class': 'form-control'}),
            'edu_doc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'edu_doc_date': forms.DateInput(attrs={'class': 'form-control'}),
            'tab_number': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control'}),
            'fire_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
