from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message form {self.name} at {self.sent_at.strftime('%Y-%m-%d %H:%M')}"