from django.shortcuts import render
from rest_framework import viewsets
from .models import Knihovna
from .serializers import KnihovnaSerializer



class KnihovnaViewSet(viewsets.ModelViewSet):
    queryset = Knihovna.objects.all()
    serializer_class = KnihovnaSerializer
