from django.db import models

class Movies(models.Model):
    """Detail of each movies"""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cineme = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title}"

class ShowTimes(models.Model):
    """Show times of each movies"""

    movies = models.ForeignKey(Movies, related_name="Showtimes", on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return f"{self.start_time}"


