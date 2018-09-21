from datetime import datetime

from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from model_utils.models import TimeStampedModel, StatusModel

STATUS = [
    ("open", "Open"),
    ("submitted", "Submitted"),
    ("claimed", "Claimed"),
    ("graded", "Graded"),
    ("sent", "Feedback Sent"),
]


class Cohort(TimeStampedModel, models.Model):
    """Cohort."""

    id = models.SlugField(
        max_length=10,
        primary_key=True,
    )

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("cohort_detail", kwargs={"pk": self.id})


class Student(TimeStampedModel, models.Model):
    """Student."""

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        max_length=50,
    )

    cohort = models.ForeignKey("Cohort", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.id})


class Assessment(TimeStampedModel, models.Model):
    """Assessment."""

    id = models.SlugField(
        max_length=50,
        primary_key=True,
    )

    title = models.CharField(
        max_length=50,
        unique=True,
    )

    notes = models.TextField(
        help_text="Staff-only notes.",
        blank=True,
    )

    def __str__(self):
        return self.title


class AssessmentSession(TimeStampedModel, models.Model):
    """Assessment in a cohort."""

    assessment = models.ForeignKey("Assessment", on_delete=models.CASCADE)

    cohort = models.ForeignKey("Cohort", on_delete=models.CASCADE)

    due_at = models.DateTimeField()

    notes = models.TextField(
        help_text="Staff-only notes.",
        blank=True,
    )

    class Meta:
        unique_together = ['assessment', 'cohort']

    def __str__(self):
        return f"{self.assessment} / {self.cohort_id}"

    def get_absolute_url(self):
        return reverse("assessmentsession_detail", kwargs={"pk": self.id})


class Submission(TimeStampedModel, StatusModel, models.Model):
    """Submission of an assessment."""

    STATUS = STATUS

    student = models.ForeignKey("Student", on_delete=models.CASCADE)

    assessmentsession = models.ForeignKey("AssessmentSession", on_delete=models.CASCADE)

    grade = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)],
        null=True,
        blank=True,
    )

    feedback = models.TextField(
        blank=True,
        help_text="Feedback that will be shared with student."
    )

    notes = models.TextField(
        help_text="Staff-only notes.",
        blank=True,
    )

    assessor = models.CharField(
        max_length=50,
        blank=True,
    )

    class Meta:
        unique_together = ["student", "assessmentsession"]

    def __str__(self):
        return f"{self.student} / {self.assessmentsession.assessment}"

    def get_absolute_url(self):
        return reverse("submission_edit", kwargs={"pk": self.id})


def submissionfile_path(instance, filename):
    student = slugify(instance.submission.student)
    date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    sess = instance.submission.assessmentsession
    return f'submissions/{sess.cohort_id}/{sess.assessment_id}/{sess.id}-{student}-{date}.zip'


class SubmissionFile(TimeStampedModel, models.Model):
    """Submission zip file."""

    submission = models.ForeignKey("Submission", on_delete=models.CASCADE)

    zipfile = models.FileField(
        upload_to=submissionfile_path,
        validators=[FileExtensionValidator(allowed_extensions=['zip'])],
    )

    comments = models.TextField(
        blank=True,
        help_text="Comments from student."
    )
