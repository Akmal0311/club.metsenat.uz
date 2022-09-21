from django.urls import path
from .views import *
urlpatterns = [
    path('sponsor/', SponsorView.as_view(), name='add_sponsor'),
    path('sponsor/<int:pk>', SponsorDetailView.as_view(), name='sponsor_detail'),
    path('sponsor_list/', SponsorListView.as_view(), name='sponsor_list'),
    path('student/', StudentView.as_view(), name='add_student'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:student_id>/add_sponsor/', SponsorPayForStudentView.as_view(), name='add_sponsor_to_student'),
    path('edit_sponsor/<int:pk>/', EditSponsorView.as_view(), name='edit_sponsor'),
    path('otm/', IHEView.as_view(), name='add_otm'),
    path('otm/<int:pk>/', IHEDetailView.as_view(), name='otm_detail'),
    path('otm_list/', IHEListView.as_view(), name='otm_list'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
