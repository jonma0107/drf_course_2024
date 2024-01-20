from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from watchlist_app.api.validators import min_max_validator
from django.contrib.auth.models import User

# Create your models here.


class StreamPlataform(models.Model):
  name = models.CharField(max_length=50)
  about = models.CharField(max_length=150)
  website = models.URLField(max_length=100)

  def __str__(self):
    return self.name


class Movie(models.Model):
  title = models.CharField(max_length=100)
  storyline = models.CharField(max_length=200)
  platform = models.ForeignKey(
      StreamPlataform,
      on_delete=models.CASCADE,
      related_name="movies")
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


class Review(models.Model):
  reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField(validators=[min_max_validator])
  description = models.CharField(max_length=200)
  movie = models.ForeignKey(
      Movie,
      on_delete=models.CASCADE,
      related_name="reviews")
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.rating) + " | " + self.movie.title
