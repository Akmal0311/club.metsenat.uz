from django.urls import path
from . import views


urlpatterns = [
    path('sponsor/', views.SponsorView.as_view(), name='add_sponsor'),
    path('sponsor/<int:pk>', views.SponsorDetailView.as_view(), name='sponsor_detail'),
    path('sponsor_list/', views.SponsorListView.as_view(), name='sponsor_list'),
    path('student/', views.StudentView.as_view(), name='add_student'),
    path('student_list/', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:student_id>/add_sponsor/', views.SponsorPayForStudentView.as_view(), name='sponsor_to_student'),
    path('edit_sponsor/<int:pk>/', views.EditSponsorView.as_view(), name='edit_sponsor'),
    path('otm/', views.OTMView.as_view(), name='add_otm'),
    path('otm/<int:pk>/', views.OTMDetailView.as_view(), name='otm_detail'),
    path('otm_list/', views.OTMListView.as_view(), name='otm_list'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
]
