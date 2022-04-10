from django.shortcuts import render
from .models import Words
from rest_framework import generics
from .serializer import WordsSerializer

# Create your views here.
class WordsList(generics.ListAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

class WordsCreate(generics.CreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

class WordsRetrieve(generics.RetrieveAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    lookup_field = 'word'

class WordsUpdate(generics.RetrieveUpdateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer

class WordsDelete(generics.DestroyAPIView):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer