from django.db import models
from django.contrib.auth import get_user_model
from datetime import date, timedelta, datetime

User = get_user_model()
next_3_days = datetime.now() + timedelta(days=3)
PRIORITIES = (
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High")
)
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateField(default= next_3_days)
    completed = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITIES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('completed','priority', 'due_date', )

    # def total_tasks(self):
    #     return self.count()

    def __str__(self):
        return self.title
    