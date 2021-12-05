from django.db.models.base import Model
from rest_framework import response, serializers
from rest_framework import fields
from rest_framework.response import responses
from rest_framework.fields import ReadOnlyField

from movies.models import  ContentList,StreamingPlatform


import datetime



# x = datetime.date.today()


# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     release = serializers.DateField()


#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get("name",instance.name)
#         instance.description = validated_data.get("description",instance.description)
#         instance.release = validated_data.get("release",instance.release)

#         instance.save()

#         return instance


class ContentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContentList
        fields = '__all__'
        # exclude = ["relase"]


class StreamingPlatformSerializers(serializers.ModelSerializer):
    content_list = ContentListSerializers(many =True , read_only = True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'
