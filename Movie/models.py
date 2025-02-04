from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
