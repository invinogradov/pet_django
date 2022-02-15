from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.db.models.functions import Concat
from django.db.models import Value

from .forms import *
from .models import *


class ObejctView:
    @staticmethod
    def find_by_doc(search_str, obj):
        queryset = obj.objects.annotate(
            doc=Concat('face__doc_series', Value(' '), 'face__doc_number'))
        return queryset.filter(doc__icontains=search_str)

    @staticmethod
    def find_by_inn(search_str, obj):
        return obj.objects.filter(face__inn__icontains=search_str)

    @staticmethod
    def find_by_snils(search_str, obj):
        return obj.objects.filter(face__snils__icontains=search_str)

    @staticmethod
    def find_by_fio(search_str, obj):
        queryset = obj.objects.annotate(
            fio=Concat('face__surname', Value(' '), 'face__name', Value(' '), 'face__patronymic'))
        return queryset.filter(fio__icontains=search_str)

    @staticmethod
    def find_by_phone(search_str, obj):
        return obj.objects.filter(face__phone__icontains=search_str)

    @staticmethod
    def find_by_required_medical_policy(search_str, obj):
        return obj.objects.filter(required_medical_policy__icontains=search_str)

    @staticmethod
    def find_by_add_medical_policy(search_str, obj):
        return obj.objects.filter(add_medical_policy__icontains=search_str)

    @staticmethod
    def find_by_speciality(search_str, obj):
        for i in SPECIALITY:
            if search_str.lower() in i[1].lower():
                return obj.objects.filter(speciality=i[0])
        return obj.objects.none()

    @staticmethod
    def find_by_post(search_str, obj):
        for i in POST:
            if search_str.lower() in i[1].lower():
                return obj.objects.filter(post=i[0])
        return obj.objects.none()


class AddPatient(CreateView):
    model = Patients
    form_class = PatientForm
    context_object_name = 'patient'
    template_name = 'manager_workplace/add_patient.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.face_id = self.kwargs.get('face')
        fields.save()
        return super().form_valid(form)


class PatientsList(ListView, ObejctView):
    model = Patients
    template_name = 'manager_workplace/patients_list.html'
    context_object_name = 'patients'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def get_queryset(self):
        if not self.request.GET.get('search_str'):
            return Patients.objects.all()
        else:
            return (self.find_by_doc(self.request.GET.get('search_str'), Patients) |
                    self.find_by_inn(self.request.GET.get('search_str'), Patients) |
                    self.find_by_snils(self.request.GET.get('search_str'), Patients) |
                    self.find_by_fio(self.request.GET.get('search_str'), Patients) |
                    self.find_by_phone(self.request.GET.get('search_str'), Patients) |
                    self.find_by_required_medical_policy(self.request.GET.get('search_str'), Patients) |
                    self.find_by_add_medical_policy(self.request.GET.get('search_str'), Patients)).distinct()


class PatientCard(DetailView):
    model = Patients
    context_object_name = 'patient'
    template_name = 'manager_workplace/patient_card.html'


class AddFace(CreateView):
    model = Faces
    form_class = FaceForm
    context_object_name = 'face'
    template_name = 'manager_workplace/add_face.html'
    # success_url = 'add_patient'

    def get_success_url(self):
        return reverse(self.request.path[1:-6], kwargs={'face': self.object.pk})


class FacesList(ListView, ObejctView):
    model = Faces
    template_name = 'manager_workplace/faces_list.html'
    context_object_name = 'faces'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        response = HttpResponse('blah')
        response.set_cookie('cookie_name', 'cookie_value')
        test = self.request.META['HTTP_REFERER']
        if test.endswith('doctors_list/') or test.endswith('staff_list/'):
            context['next_url'] = 'add_staff'
        else:
            context['next_url'] = 'add_patient'
        return context

    def get_queryset(self):
        if not self.request.GET.get('search_str'):
            return Faces.objects.all()
        else:
            return (self.find_by_doc(self.request.GET.get('search_str'), Faces) |
                    self.find_by_inn(self.request.GET.get('search_str'), Faces) |
                    self.find_by_snils(self.request.GET.get('search_str'), Faces) |
                    self.find_by_fio(self.request.GET.get('search_str'), Faces) |
                    self.find_by_phone(self.request.GET.get('search_str'), Faces)).distinct()


class FaceCard(DetailView):
    model = Faces
    context_object_name = 'face'
    template_name = 'manager_workplace/face_card.html'


class AddStaff(CreateView):
    model = Staff
    form_class = StaffForm
    context_object_name = 'staff'
    template_name = 'manager_workplace/add_staff.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.face_id = self.kwargs.get('face')
        fields.save()
        return super().form_valid(form)


class DoctorsList(ListView, ObejctView):
    model = Staff
    template_name = 'manager_workplace/doctors_list.html'
    context_object_name = 'doctors'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def get_queryset(self):
        if not self.request.GET.get('search_str'):
            return Staff.objects.filter(post=0)
        else:
            return (self.find_by_fio(self.request.GET.get('search_str'), Staff) |
                    self.find_by_speciality(self.request.GET.get('search_str'), Staff)).filter(post=0)


class StaffCard(DetailView):
    model = Staff
    context_object_name = 'staff'
    template_name = 'manager_workplace/staff_card.html'


class StaffList(ListView, ObejctView):
    model = Staff
    template_name = 'manager_workplace/staff_list.html'
    context_object_name = 'staff'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def get_queryset(self):
        if not self.request.GET.get('search_str'):
            return Staff.objects.exclude(post=0)
        else:
            return (self.find_by_fio(self.request.GET.get('search_str'), Staff) |
                    self.find_by_post(self.request.GET.get('search_str'), Staff)).exclude(post=0)


class AddVisit(CreateView):
    model = Visits
    form_class = VisitForm
    context_object_name = 'visit'
    template_name = 'manager_workplace/add_visit.html'


class VisitCard(DetailView):
    model = Visits
    context_object_name = 'visit'
    template_name = 'manager_workplace/visit_card.html'


class VisitList(ListView):
    model = Visits
    context_object_name = 'visits'
    template_name = 'manager_workplace/visits_list.html'

    def get_queryset(self):
        if self.kwargs.get('patient'):
            return Visits.objects.filter(patient=self.kwargs['patient'])
        elif self.kwargs.get('doctor'):
            return Visits.objects.filter(doctor=self.kwargs['doctor'])

# def add_patient(request):
#     if request.method == 'POST':
#         p_form = PatientForm(request.POST, instance=Patients())
#         f_form = FaceForm(request.POST, instance=Faces())
#         if p_form.is_valid() and f_form.is_valid():
#             new_face = f_form.save()
#             new_patient = p_form.save(commit=False)
#             new_patient.face = new_face
#             new_patient.save()
#             return redirect(new_patient)
#     else:
#         p_form = PatientForm(instance=Patients())
#         f_form = FaceForm(instance=Faces())
#
#     return render(request, 'manager_workplace/add_patient.html',
#                   {'face_form': f_form, 'patient_form': p_form})
#
#
# def add_face(request):
#     if request.method == 'POST':
#         f_form = FaceForm(request.POST, instance=Faces())
#         if f_form.is_valid():
#             face = f_form.save()
#             # asd = PatientForm()
#             # asd.instance.face = face
#             # return render(request, 'manager_workplace/add_patient.html', {'form': asd})
#             return redirect('add_patient', )
#     else:
#         f_form = FaceForm()
#     return render(request, 'manager_workplace/add_face.html', {'form': f_form})
