from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('registrations/', views.list_registrations,name='list_registrations'),
    path('update/<int:pk>/', views.update_registration, name='update_registration'),
    path('delete/<int:pk>/', views.delete_registration, name='delete_registration'),
    path('practice',views.practice,name= "practice")
]