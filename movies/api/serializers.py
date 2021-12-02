from rest_framework import response, serializers
from rest_framework.response import responses
from rest_framework.fields import ReadOnlyField
import datetime



x = datetime.date.today()


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    release = serializers.DateField()
