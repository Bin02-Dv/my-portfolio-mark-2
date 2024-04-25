from django.db import models

# Create your models here.

class ContactMe(models.Model):
    name = models.CharField(max_length=225, blank=True)
    email = models.EmailField(unique=True, max_length=225, blank=True)
    subject = models.CharField(max_length=225, blank=True)
    message = models.TextField(max_length=225, blank=True)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} - {self.subject}"
