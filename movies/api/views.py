

from rest_framework import serializers,status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView


from movies.models import ContentList,StreamingPlatform
from movies.api.serializers import ContentListSerializers,StreamingPlatformSerializers


@api_view(["GET","POST"])
def content_list(request):
    
    if request.method == 'GET':
        movies = ContentList.objects.all()
        serializer = ContentListSerializers(movies,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ContentListSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET","DELETE","PUT"])
def content_details(request,pk):

    if request.method == 'GET':
        try:
            movie = ContentList.objects.get(pk=pk)
            serializer = ContentListSerializers(movie)
            return Response(serializer.data)
        except ContentList.DoesNotExist:
            return Response({"No data to show "}, status = status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        movie = ContentList.objects.get(pk=pk)
        serializer = ContentListSerializers(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors)
    if request.method == "DELETE":
        movie = ContentList.objects.get(pk=pk)
        movie.delete()

        return Response({"Your requested item is deleted"}, status = status.HTTP_204_NO_CONTENT)

class StreamingPlatformAV(APIView):
    

    def get(self, request):
        platform = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializers(platform, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = StreamingPlatformSerializers(data = request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)


class StreamingPlatformDtails(APIView):

    def get(self,request,pk):
        try:
            streamplatform = StreamingPlatform.objects.get(pk=pk)
            serializer = StreamingPlatformSerializers(streamplatform)
            return Response(serializer.data)
        except StreamingPlatform.DoesNotExist:
            return Response({"platform does not exist"}, status = status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        streamplatform = StreamingPlatform.objects.get(pk=pk)
        serializer =  StreamingPlatformSerializers(streamplatform,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"Something is wrong!"}, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        data = StreamingPlatform.objects.get(pk=pk)
        data.delete()
        return Response({"item is deleted"},status = status.HTTP_200_OK)

