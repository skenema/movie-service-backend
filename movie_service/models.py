from django.db import models

class Movie(models.Model):
    """Detail of each movies"""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cinema = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title}"

