from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers,models,permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
# Create your views here.

class HelloApiView(APIView):
    """Class for testing our API"""
    serializer_class = serializers.HelloViewSerializer
    def get(self, request , format = None):
        """ rest framework get function """
        an_apiview = [
        'Advantages of Django',
        'Complex to learn',
        'Bla Bla Bla...'
        ]

        return Response({'message' : 'Test API','an api view': an_apiview})
    def put(self, response, pk = None):
        return Response({'message':'A PUT Request'})

    def patch(self, response, pk = None):
        return Response({'message':'A PATCH Request'})

    def delete(self, response, pk = None):
        return Response({'message':'A delete Request'})

    def post(self,request):
        """ post function for rest framework """
        serializer = serializers.HelloViewSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            message = "Hello "+ str(name) + " your email is "+str(email)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class HelloViewSet(viewsets.ViewSet):
    """" A Test ViewSet Class """
    def list(self,response):
        a = [
        "List function in ViewSet",
        "Testng purpose",
        "bla bla bla",
        ]
        return Response({'message':'Hello',"List":a})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateUserProfile,)
