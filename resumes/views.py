from django.views import generic

from .models import Resume


class ResumeList(generic.ListView):
    model = Resume
    context_object_name = "resume_list"


class ResumeDetail(generic.DetailView):
    model = Resume
    context_object_name = "resume_detail"
