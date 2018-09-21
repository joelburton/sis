from django.contrib import admin

from assessments.models import Submission, Cohort, Assessment, AssessmentSession, Student, SubmissionFile


@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    """Cohort admin."""


@admin.register(Assessment)
class AsessmentAdmin(admin.ModelAdmin):
    """Assessment admin."""


@admin.register(AssessmentSession)
class AssessmentSessionAdmin(admin.ModelAdmin):
    """Assessment Session admin."""

    list_display = ['id', 'cohort', 'assessment', 'due_at']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Student admin."""


class SubmissionFileInline(admin.TabularInline):
    model = SubmissionFile


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """Admin for submissions."""

    list_display = ['id', 'assessmentsession', 'student', 'status']
    inlines = [SubmissionFileInline]
