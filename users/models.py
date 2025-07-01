from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    @property
    def number_of_tasks(self):
        if hasattr(self, 'tasks'):
            return self.tasks.count()
        return 0
