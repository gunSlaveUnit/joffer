from django.views import generic

from .models import Resume


class ResumeList(generic.ListView):
    model = Resume
    context_object_name = "resume_list"
