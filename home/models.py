from django.db import models


class Event(models.Model):
    TAG_CHOICES = [
        ('nunta', 'Nunta'),
        ('botez', 'Botez'),
        ('majorat', 'Majorat'),
        ('altele', 'Alte Evenimente'),
    ]

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    youtube_link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='altele')

    def __str__(self):
        return self.name