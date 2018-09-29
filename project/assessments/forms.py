from django import forms
from django.forms import Textarea, DateTimeInput

from assessments.models import SubmissionFile, Submission


class SubmissionForm(forms.ModelForm):
    """Form for editing a submission."""

    class Meta:
        model = Submission
        fields = ["status", "status_changed", "grade", "feedback", "notes", "assessor"]
        widgets = {
            "status_changed": DateTimeInput(attrs={'readonly': True}),
            'notes': Textarea(attrs={'cols': 80, 'rows': 16}),
            'feedback': Textarea(attrs={'cols': 80, 'rows': 16}),
        }


class SubmissionFileForm(forms.ModelForm):
    """Form for submitting a submission file."""

    class Meta:
        model = SubmissionFile
        fields = ["submission", "zipfile", "comments"]
        widgets = {
            'comments': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
        labels = {
            'submission': 'Student',
        }
        help_texts = {
            'submission': 'Please select yourself',
            'comments': 'Comments you want to share with staff',
            'zipfile': 'Your entire submission in a single .zip file',
        }

    # submission = models.ForeignKey("Submission", on_delete=models.CASCADE)
    #
    # zipfile = models.FileField(
    #     upload_to=submissionfile_path,
    #     validators=[FileExtensionValidator(allowed_extensions=['zip'])],
    #     help_text="Entire solution in a .zip file.",
    # )
    #
    # comments = models.TextField(
    #     blank=True,
    #     help_text="Comments you want to share with with staff."
    # )
