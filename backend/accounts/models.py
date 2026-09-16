from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES=(
        ("admin","Admin"),
        ("editor","Editor"),
        ("reader","Reader")
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    email=models.EmailField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.username
