from rest_framework import serializers
from watchlist_app.api.validators import title_length
from watchlist_app.models import Movie, StreamPlataform

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   title = serializers.CharField(validators=[title_length]) # Validadores
#   description = serializers.CharField()
#   active = serializers.BooleanField()
  
  # Validador a nivel de objetos
#   def validate(self, data):
#       if data['title'] == data['description']:
#           raise serializers.ValidationError('Title and Description should be different')
#       return data
  
  # Validador a nivel de campos
#   def validate_description(self, value):
#       if len(value) <= 2:
#           raise serializers.ValidationError('Description must be more than 2 characters')
#       return value

class StreamPlataformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlataform
        fields = '__all__'
    

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' 
		
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    #         # return super().create(validated_data)     

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
	
	
	
	  