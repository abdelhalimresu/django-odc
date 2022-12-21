from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.fields.CharField(max_length=64)
    email = models.fields.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email