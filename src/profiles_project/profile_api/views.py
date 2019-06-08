from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import filters
from . import serializers,models,permissions
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
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
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """ returns a authentication token response """
    serializer_class = AuthTokenSerializer
    def create(self,request):
        print("inside")
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        print("Valid")
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class ProfileFeedItemViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnItem,IsAuthenticated)
    def perform_create(self,serializer):
        request = self.request
        self.serializer_class(data = request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        print(request.user)
        serializer.save(user_profile = request.user)
