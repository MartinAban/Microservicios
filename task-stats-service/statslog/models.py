from django.db import models

# Create your models here.
class CompletedTaskLog(models.Model):
    title = models.CharField(max_length=200)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (completado)"