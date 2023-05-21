from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image
import os

class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    IMAGE_MAX_SIZE = (300, 300)
    
    def image_resize(self):
        # Fonction pour le redimensionnement de l'image
        if self.image:
            with Image.open(self.image) as image:
                image.thumbnail(self.IMAGE_MAX_SIZE)
                image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        # Fonction pour sauvegarder avec le redimensionnement
        super().save(*args, **kwargs)
        self.image_resize()
    
    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Review(models.Model):
    class Rating(models.IntegerChoices):
        ZERO = 0, '☆☆☆☆☆'
        ONE = 1, '★☆☆☆☆'
        TWO = 2, '★★☆☆☆'
        THREE = 3, '★★★☆☆'
        FOUR = 4, '★★★★☆'
        FIVE = 5, '★★★★★'
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        choices=Rating.choices,
        default=Rating.ZERO,
        verbose_name="Note"
        )
    headline = models.CharField(max_length=128, verbose_name="Titre de la critique")
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name="followed_by")
    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)
