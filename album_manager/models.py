from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=30, null=False)
    year = models.PositiveIntegerField(null=False, default=1)
    genre = models.CharField(max_length=30, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover_image')

    def __str__(self) -> str:
        return self.title