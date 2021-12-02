

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

from movies.models import Movie
from movies.api.serializers import MovieSerializers


@api_view(["GET",])
def movie_list(request):
    
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies,many=True)

    return Response(serializer.data)


@api_view(["GET","POST"])
def movie_details(request,pk):

    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializers(movie)

    return Response(serializer.data)