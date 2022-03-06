from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path

#Importaciones de modelos
from UserProfile.models import TablaProfile

#Importaciones de serializadores
from UserProfile.serializers import TablaProfileSerializer

# Create your views here.
class TablaProfileList(APIView):
    def get(self,request,format=None):
        queryset=TablaProfile.objects.all()
        serializer = TablaProfileSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        # if 'url_img' not in request.data:
        #     raise exceptions.ParseError(
        #         "Ningun archivo")
        # url_img = request.data['url_img']
        # id_user_id=request.data['id_user_id']
        serializer=TablaProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            validated_data = serializer.validated_data
            img = TablaProfile(**validated_data)
            # img.save()
            serializer_response = TablaProfileSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TablaProfileDetail(APIView):
    def get_object(self,pk):
        try:
            return TablaProfile.objects.get(pk=pk)
        except TablaProfile.DoesNotExist:
            return "No existe"
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != "No existe":
            idResponse = TablaProfileSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos",status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = TablaProfileSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    
