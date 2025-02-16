from django.urls import path
from .views import average_salary_python_jobs

urlpatterns = [
    path('average_salary/', average_salary_python_jobs, name='average_salary'),
]
