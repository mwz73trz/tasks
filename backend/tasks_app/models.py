from email.policy import default
from random import choices
from django.db import models

class Task(models.Model):
    INITIAL = 'Initial'
    IN_PROGRESS = 'In Progress'
    ON_HOLD = 'On Hold'
    COMPLETED = 'Completed'
    STATUSES = [
        (INITIAL, 'Initial'),
        (IN_PROGRESS, 'In Progress'),
        (ON_HOLD, 'On Hold'),
        (COMPLETED, 'Completed')
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=265)
    status = models.CharField(choices=STATUSES, default=INITIAL, max_length=20)
    notes = models.TextField(null=True, blank=True)
    due_by = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

