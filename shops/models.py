from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    CATEGORY_CHOICES = [
        ('Coffee', 'Coffee'),
        ('Food', 'Food'),
        ('Fashion', 'Fashion'),
        ('Tech', 'Tech'),
        ('Art', 'Art'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Coffee'
    )

    likes = models.ManyToManyField(
        User,
        related_name='liked_shops',
        blank=True,
    )

    favorites = models.ManyToManyField(
    User,
    related_name='favorite_shops',
    blank=True
)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
    