from django.contrib import admin


from .models import Patients, Faces, Staff

admin.site.register(Patients)
admin.site.register(Faces)
admin.site.register(Staff)
