from django.shortcuts import render
from .models import Slideshow, News, Companies, Exp
from .serializers import SlideSerializer, NewsSerializer, CompSerializer, ExpSerializer, ExpDetailSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
class SlideViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Slideshow.objects.all()
    serializer_class = SlideSerializer

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CompViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Companies.objects.all().order_by('name')
    serializer_class = CompSerializer

class ExpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exp.objects.all().order_by('name')
    serializer_class = ExpSerializer

@api_view(['GET'])
def FTE_list(request, company):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        exps = Exp.objects.filter(placement = 'FTE', name = company)
        serializer = ExpDetailSerializer(exps, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def intern_list(request, company):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        exps = Exp.objects.filter(placement = 'Intern', name = company)
        serializer = ExpDetailSerializer(exps, many=True)
        return Response(serializer.data)
