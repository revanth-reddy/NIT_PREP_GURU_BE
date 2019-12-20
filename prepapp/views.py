from django.shortcuts import render
from .models import Slideshow
from .serializers import SlideSerializer
from rest_framework import viewsets

# Create your views here.
class SlideViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Slideshow.objects.all()
    serializer_class = SlideSerializer