from django.http import JsonResponse
from rest_framework import serializers,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET','POST'])
def movie_list(request,format = None):

    if request.method =='GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def movie_details(request,id, format = None):
 
    try:
        movie = MovieSerializer.objects.get(pk=id)
    except Movie.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

            
# {
#     "name":"URI",
#     "description": "a war ridden movie"
# }