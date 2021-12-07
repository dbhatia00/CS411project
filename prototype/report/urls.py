from django.urls import path
from report import views

urlpatterns = [
    path('report/', views.report, name='report'),
]