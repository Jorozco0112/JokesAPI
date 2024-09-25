from rest_framework import serializers

from jokes.models import Joke

class JokeSerializer(serializers.ModelSerializer):
    "This class serialize joke entity"
    class Meta:
        model = Joke
        fields = ("id", "description")
