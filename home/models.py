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

from django.db import models

class Review(models.Model):
    CLIENT = 'client'
    COLEG = 'coleg'
    ROLE_CHOICES = [
        (CLIENT, 'Client'),
        (COLEG, 'Coleg'),
    ]

    PENDING = 'pending'
    APPROVED = 'approved'
    DENIED = 'denied'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
    ]

    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='reviews/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CLIENT)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)  # Câmp pentru status

    def __str__(self):
        return f"Review by {self.name} ({self.get_role_display()}) on {self.created_at.strftime('%Y-%m-%d')}"
