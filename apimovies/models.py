from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)  # Change 'name' to 'title' for clarity
    description = models.TextField()  # Allowing for longer descriptions
    # release_date = models.DateField()
    # genre = models.CharField(max_length=100)
    # director = models.CharField(max_length=100)
    # # actors = models.ManyToManyField("Actors" , related_name='movies')
    # duration_minutes = models.PositiveIntegerField()
    # poster_url = models.URLField()
    # trailer_url = models.URLField()
    
    def __str__(self) -> str:
        return self.name