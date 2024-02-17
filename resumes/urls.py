from django.urls import path

from .views import ResumeList, ResumeDetail

urlpatterns = [
    path('', ResumeList.as_view(), name='resume_list'),
    path('<int:pk>/', ResumeDetail.as_view(), name='resume_detail'),
]
