from django.http import JsonResponse
from .models import Job
import numpy as np

def average_salary_python_jobs(request):
    jobs = Job.objects.filter(title__icontains="Python", location__icontains="Lucknow")  
    salaries = [job.salary for job in jobs if job.salary is not None]
    
    if salaries:
        avg_salary = np.mean(salaries)
        return JsonResponse({"average_salary": avg_salary})
    else:
        return JsonResponse({"message": "No salary data available."})
