from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Class for testing our API"""

    def get(self, request , format = None):
        """ rest framework get function """
        an_apiview = [
        'Advantages of Django',
        'Complex to learn',
        'Bla Bla Bla...'
        ]

        return Response({'message' : 'Test API','an api view': an_apiview})
