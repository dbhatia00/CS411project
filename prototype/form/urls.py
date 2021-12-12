from django.urls import path
from form import views

urlpatterns = [
    path('', views.login, name='login'),
    path('form/', views.form, name='form'),
    path('report/', views.report,name='report')
]
