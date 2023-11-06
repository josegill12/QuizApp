from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

class UserList(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

   async def list(self, request, *args, **kwargs):
       queryset = await self.get_queryset()
       serializer = UserSerializer(queryset, many=True)
       return Response(serializer.data)

   async def create(self, request, *args, **kwargs):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           await serializer.save()
           return Response(serializer.data, status=201)
       return Response(serializer.errors, status=400)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer

   async def retrieve(self, request, *args, **kwargs):
       instance = await self.get_object()
       serializer = UserSerializer(instance)
       return Response(serializer.data)

   async def update(self, request, *args, **kwargs):
       instance = await self.get_object()
       serializer = UserSerializer(instance, data=request.data)
       if serializer.is_valid():
           await serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=400)

   async def destroy(self, request, *args, **kwargs):
       instance = await self.get_object()
       await instance.delete()
       return Response(status=204)
   
class CreateTokenView(ObtainAuthToken):
    

    """Views for authorizations"""

    serializer_class = AuthTokenSerializer
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        serializedUser = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'location': user.location,
            'pitch': user.pitch,
            'tags': serializedUser.data.get('tags'),
            'profile_image': serializedUser.data.get('profile_image'),
        })