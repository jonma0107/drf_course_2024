from django.db import models

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
