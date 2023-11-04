from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

from rest_framework.response import Response

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