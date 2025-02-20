from rest_framework import serializers

from animes.models import Anime, AnimeMovie, AnimeCharacter
from base.models import Category



class CategorySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = '__all__'


    
class AnimeCharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnimeCharacter
        exclude = ('is_active', 'is_favorite')

    
    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'name': instance.name,
            'age': instance.age,
            'image': instance.image.url if instance.image else None,
            'info': instance.info
        }

        # Verificar si anime está presente
        if instance.anime:
            representation['anime'] = instance.anime.name
        else:
            representation['anime'] = None
        
        # Verificar si anime_movie está presente
        if instance.anime_movie:
            representation['anime-movie'] = instance.anime_movie.name
        else:
            representation['anime-movie'] = None

        return representation

class AnimeMovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = AnimeMovie
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'rating': instance.rating,
            'category': instance.category.name,
            'duration': instance.duration,
            'image': instance.image.url,
            'sinopsis': instance.sinopsis, 
        }
    

class AnimeSerializer(serializers.ModelSerializer):

    anime_characters = AnimeCharacterSerializer(many = True, read_only = True)


    class Meta:
        model = Anime
        exclude = ('is_active', 'is_favorite')
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name
        representation['image'] = instance.image.url

        return representation


    