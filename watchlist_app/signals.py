from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Review

@receiver(post_delete, sender=Review)
def update_movie_number_rating(sender, instance, **kwargs):
    movie = instance.movie
    movie.number_rating = models.F('number_rating') - 1
    movie.avg_rating = movie.avg_rating-instance.rating
    movie.save()

 
