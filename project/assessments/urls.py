from django.urls import path

from . import views

urlpatterns = [
    path('session/<int:pk>/', views.AssessmentSessionDetailView.as_view(), name="assessmentsession_detail"),
    path('submission/<int:pk>/', views.SubmissionUpdateView.as_view(), name="submission_edit"),
    path('submit/<int:assessmentsession_id>/', views.SubmissionFileCreateView.as_view(), name="submission_submit"),
]
