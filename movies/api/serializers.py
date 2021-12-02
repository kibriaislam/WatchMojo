from rest_framework import response, serializers
from rest_framework.response import responses
from rest_framework.fields import ReadOnlyField

from movies.models import Movie


import datetime



x = datetime.date.today()


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    release = serializers.DateField()


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.description = validated_data.get("description",instance.description)
        instance.release = validated_data.get("release",instance.release)

        instance.save()

        return instance

