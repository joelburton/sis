from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from assessments.forms import SubmissionForm, SubmissionFileForm
from assessments.models import SubmissionFile, AssessmentSession, Cohort, Submission, Student


class SubmissionFileCreateView(generic.CreateView):
    """Add submission file."""

    model = SubmissionFile
    form_class = SubmissionFileForm
    success_url = "/assessments/thanks/"

    def get_form(self, form_class=None):
        """Override form to handle custom choices for student."""

        form = super().get_form(form_class)
        form.fields['submission'].queryset = Submission.objects.filter(
                assessmentsession=self.kwargs['assessmentsession_id'])
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assessment_session'] = AssessmentSession.objects.get(pk=self.kwargs['assessmentsession_id'])

        return context

class SubmissionFileThanksView(generic.TemplateView):
    """Acknowledge receipt."""

    template_name = "assessments/thanks.html"


class CohortDetailView(LoginRequiredMixin, generic.DetailView):
    """List of session assessments."""

    model = Cohort


class AssessmentSessionDetailView(LoginRequiredMixin, generic.DetailView):
    """List of submissions for an assessment session."""

    model = AssessmentSession


class SubmissionUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Edit a submission."""

    model = Submission
    form_class = SubmissionForm

    def get_success_url(self):
        return self.object.assessmentsession.get_absolute_url()


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    """Detail for student."""

    model = Student


class CohortListView(LoginRequiredMixin, generic.ListView):
    """List of cohorts."""

    model = Cohort
