from rest_framework import serializers

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   title = serializers.CharField()
#   description = serializers.CharField()
#   active = serializers.BooleanField()


from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' 
        
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
        # return super().create(validated_data)     

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance