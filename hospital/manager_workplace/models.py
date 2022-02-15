from django.db import models
from django.urls import reverse
from .choices import *


class Faces(models.Model):
    surname = models.CharField(max_length=35, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=35, verbose_name='Отчество', blank=True, null=True)
    gender = models.IntegerField(choices=GENDER, verbose_name='Пол')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    doc_type = models.IntegerField(choices=DOC_TYPE, verbose_name='Тип документа')
    doc_series = models.CharField(max_length=10, verbose_name='Документ серия')
    doc_number = models.CharField(max_length=15, verbose_name='Документ номер')
    doc_date = models.DateField(verbose_name='Документ дата выдачи')
    doc_given = models.CharField(max_length=150, verbose_name='Документ выдан')
    doc_code_division = models.CharField(max_length=15, verbose_name='Документ код подразделения', blank=True, null=True)
    snils = models.CharField(max_length=20, verbose_name='СНИЛС', unique=True)
    inn = models.CharField(max_length=12, verbose_name='ИНН', unique=True)
    registration = models.CharField(max_length=250, verbose_name='Адрес регистрации')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    notes = models.TextField(verbose_name='Заметки', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def get_absolute_url(self):
        return reverse('face_card', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Физ.лицо'
        verbose_name_plural = 'Физ.лица'
        unique_together = ('doc_type', 'doc_series', 'doc_number', 'doc_date')


class Patients(models.Model):
    face = models.ForeignKey('Faces', on_delete=models.PROTECT, verbose_name='Физ.лицо')
    blood_type = models.IntegerField(choices=BLOOD_TYPE, verbose_name='Группа крови', blank=True, null=True)
    hiv_status = models.IntegerField(choices=HIV_STATUS, verbose_name='ВИЧ статус', blank=True, null=True)
    height = models.IntegerField(verbose_name='Рост', blank=True, null=True)
    weight = models.IntegerField(verbose_name='Вес', blank=True, null=True)
    allergies = models.TextField(verbose_name='Аллергии', blank=True, null=True)
    required_medical_policy = models.CharField(max_length=30, verbose_name='Полис ОМС', unique=True)
    add_medical_policy = models.CharField(max_length=30, verbose_name='Полис ДМС', blank=True, unique=True, null=True)
    notes = models.TextField(verbose_name='Заметки', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def get_absolute_url(self):
        return reverse('patient_card', kwargs={"pk": self.pk})

    def __str__(self):
        return f'Пациент {self.face.__str__()}'

    class Meta:
        verbose_name = 'Пацаент'
        verbose_name_plural = 'Пациенты'


class Staff(models.Model):
    face = models.ForeignKey(Faces, on_delete=models.PROTECT, verbose_name='Физ.лицо')
    post = models.IntegerField(choices=POST, verbose_name='Должность')
    speciality = models.IntegerField(choices=SPECIALITY, verbose_name='Специальность', blank=True, null=True)
    education_document = models.IntegerField(choices=EDU_DOC_TYPE, verbose_name='Докумнет об образовании', blank=True, null=True)
    edu_doc_series = models.CharField(max_length=10, verbose_name='Документ серия', blank=True, null=True)
    edu_doc_number = models.CharField(max_length=10, verbose_name='Документ номер', blank=True, null=True)
    edu_doc_date = models.DateField(verbose_name='Документ дата', blank=True, null=True)
    tab_number = models.CharField(max_length=10, verbose_name='Табельный номер', unique=True)
    salary = models.FloatField(verbose_name='Оклад')
    hire_date = models.DateField(verbose_name='Дата приёма')
    fire_date = models.DateField(verbose_name='Дата увольнения', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def get_absolute_url(self):
        return reverse('staff_card', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{POST[self.post]} {self.face.__str__()}'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        unique_together = ('education_document', 'edu_doc_series', 'edu_doc_number', 'edu_doc_date')


class Visits(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.PROTECT, verbose_name='Пациент')
    doctor = models.ForeignKey(Staff, on_delete=models.PROTECT, verbose_name='Врач')
    date = models.DateField(verbose_name='Дата приёма')
    time = models.TimeField(verbose_name='Время приёма')
    previous_visit = models.ForeignKey("Visits", on_delete=models.PROTECT, verbose_name='Предыдущий визит', blank=True, null=True)
    complaint = models.TextField(verbose_name='Жалобы', null=True)
    parameters = models.TextField(verbose_name='Показатели', null=True)
    diagnosis = models.TextField(verbose_name='Диагноз', null=True)
    appointments = models.TextField(verbose_name='Назначения', null=True)
    analysis_results = models.TextField(verbose_name='Результаты анализов', blank=True, null=True)
    need_allowance = models.BooleanField(verbose_name='Требудется больничный', default=False)

    def get_absolute_url(self):
        return reverse('visit_card', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.patient.__str__()}, приём у {self.doctor.__str__()} {self.date} в {self.time}'

    class Meta:
        verbose_name = 'Приём'
        verbose_name_plural = 'Приёмы'
        unique_together = ('doctor', 'date', 'time')
