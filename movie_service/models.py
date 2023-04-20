from django.db import models

class Movie(models.Model):
    """Detail of each movies"""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cinema = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/', null=True)

    def __str__(self) -> str:
        return f"{self.title}"

