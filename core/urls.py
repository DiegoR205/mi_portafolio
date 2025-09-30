from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactame/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('fyq/', views.fyq, name='fyq'),
    path('open/', views.open_view, name='open'),
    path('open/<int:pk>/', views.open_detail, name='open_detail'),
]
