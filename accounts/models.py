from django.db import models

class SimpleUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username