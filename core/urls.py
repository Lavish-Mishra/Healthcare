from django.urls import path
from .views import (
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, PatientMappingListView, MappingDeleteView
)

urlpatterns = [
    # Patient APIs
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Doctor APIs
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    #Patient-Doctor Mapping APIs
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
    path('mappings/<int:patient_id>/doctors/', PatientMappingListView.as_view(), name='patient-doctor-list'),
]
