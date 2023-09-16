from django.http import JsonResponse
from rest_framework import serializers
from .models import *
from .serializers import *

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return JsonResponse({'movies': serializer.data},safe=False)