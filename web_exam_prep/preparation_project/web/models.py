from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from .validators import (
    TextContainsOnlyAlphaNumericAndUnderscoreValidator,
    CustomFloatPositiveValidator
)

# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(15),
            TextContainsOnlyAlphaNumericAndUnderscoreValidator()])
    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


class Album(models.Model):
    GENRE_CHOICES = [
        ("pop", "Pop Music"),
        ("jazz", "Jazz Music"),
        ("rnb", "R&B Music"),
        ("rock", "Rock Music"),
        ("country", "Country Music"),
        ("dance", "Dance Music"),
        ("hiphop", "Hip Hop Music"),
        ("other", "Other")
    ]

    album_name = models.CharField(
        blank=False, null=False, max_length=30, unique=True
    )
    artist = models.CharField(
        blank=False, null=False, max_length=30
    )
    genre = models.CharField(
        blank=False, null=False,
        max_length=30, choices=GENRE_CHOICES
    )

    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=False, null=False)
    price = models.FloatField(
        blank=False, null=False,
        validators=[CustomFloatPositiveValidator()]
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
