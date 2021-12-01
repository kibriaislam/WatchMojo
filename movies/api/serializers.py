from rest_framework import response, serializers
from rest_framework.response import responses
from rest_framework.fields import ReadOnlyField
import datetime



x = datetime.date.today()


class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.TextField()
    release = serializers.DateField()



    def validate(self, data):

        # if data['name']== data['description']:
            # return response({'Sorry You can not give Name and Description value same'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if data['release']>= x:
            return response({'Sorry You can not give relasedate in todays date or in past dates'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return data
    

    def get(self,m):
        pass