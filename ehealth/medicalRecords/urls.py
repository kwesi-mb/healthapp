from django.urls import path

from . import views

app_name = "medicalRecord"
urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
]