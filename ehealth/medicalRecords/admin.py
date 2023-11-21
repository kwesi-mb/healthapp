from django.contrib import admin
from .models import Category, medicalRecord 
# Register your models here.

admin.site.register(Category)
admin.site.register(medicalRecord)