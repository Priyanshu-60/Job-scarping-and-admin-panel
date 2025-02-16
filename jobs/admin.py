from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'job_description')  # Display these fields
    search_fields = ('title', 'company', 'location')  # Allows searching by these fields
