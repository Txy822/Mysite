from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_section_list, name='cv_section_list'),
    path('cv/<int:pk>/', views.cv_section_detail, name='cv_section_detail'),
    path('cv/new/', views.cv_section_new, name='cv_section_new'),
    ]
