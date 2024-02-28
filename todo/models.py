from django.db import models
from django_softdelete.models import SoftDeleteModel
# Create your models here.

class Task(SoftDeleteModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(null=True)
    status = models.CharField(max_length=255, choices=(('Pending', 'Pending'), ('On-going', 'ongoing'), ('Done', 'Done')), default='Pending')

    def __str__(self) -> str:
        return f"{self.title} - {self.description}"



