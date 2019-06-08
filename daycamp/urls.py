from django.urls import path
from . import views

urlpatterns = [
  # Template Views
  path('', views.landing, name='landing'),

  # API Views
  path('camper/', views.camper, name='camper'),
  path('camper/<int:pk>', views.camper_detail, name='camper_detail'),
  path('camper/<int:pk>/edit', views.camper_edit, name='camper_edit'),
  path('camper/<int:pk>/delete', views.camper_delete, name='camper_delete'),
  path('camper/new', views.camper_create, name='camper_create')
]