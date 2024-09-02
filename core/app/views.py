from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import time

# Create your views here.
@api_view(['GET'])
def index(request):
    current_time = time.ctime()
    return Response({'time': current_time})