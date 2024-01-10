from rest_framework import serializers

def title_length(value):
  if len(value) <= 2:
    raise serializers.ValidationError('Title must be more than 2 characters')
  return value