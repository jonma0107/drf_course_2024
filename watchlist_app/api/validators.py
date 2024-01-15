from rest_framework import serializers
from django.core.exceptions import ValidationError


def title_length(value):
  if len(value) <= 2:
    raise serializers.ValidationError('Title must be more than 2 characters')
  return value


def min_max_validator(value):
  if not (1 <= value <= 5):
    raise ValidationError('Rating must be between 1 and 5')
