from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import  APIView
from .models import Token
from .serializers import TokenSerializer

class MyappAPIView(generics.ListAPIView):       #api  c  выводом на специальной странице
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class List(APIView):
    def get(self, request):
        return Response()

import random
import string

class Create(media_url, owner):
    serializer_class = TokenSerializer
    def get(self, request):
        return Response()



    def generate_alphanum_random_string(20):      #генерация рандомной строки
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, 20))
        return (rand_string)



class total_supply(APIView):
    def get(self, request):
        return Response()
