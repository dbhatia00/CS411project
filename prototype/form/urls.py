from django.urls import path
from form import views

urlpatterns = [
    path('', views.login, name='login'),
    #path('form/', views.form, name='form'),
    path('form/', views.form, name='form'),
    #path('form/', views.song_title,name='')
]
