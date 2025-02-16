from djongo import models

class Job(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.FloatField(null=True, blank=True)
    job_description = models.TextField()

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.title} at {self.company}"
