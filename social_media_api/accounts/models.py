from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,  # Ensures a one-way follow relationship
        related_name="followers"
    )

    def __str__(self):
        return self.username

