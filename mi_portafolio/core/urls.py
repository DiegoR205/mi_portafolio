from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactame/', views.contactame, name='contactame'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('fyq/', views.fyq, name='fyq'),
    path('open/', views.open_list, name='open_list'),
    path('open/<int:pk>/', views.open_detail, name='open_detail'),
]
