from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username
