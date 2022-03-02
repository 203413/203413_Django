# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import exceptions
# import os.path
# from pathlib import Path

# # importaciones de modelos agregados
# from loadimage.models import TablaArchivo

# # importaciones de serializadores
# from loadimage.serializers import TablaArchivoSerializer

# # Create your views here.
# class loadImageTable(APIView):
#     def get(self, request, format=None):
#         queryset = TablaArchivo.objects.all()
#         serializer = TablaArchivoSerializer(queryset, many = True, context = {'request':request})
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         if 'url_img' not in request.data:
#             raise exceptions.ParseError(
#                 "Ningun archivo para subir")
#         archivos = request.data['url_img']
#         #archivos = Path(request.data['name_img'])
#         name, formato = os.path.splitext(archivos.name)
#         request.data['name_img'] = name
#         request.data['format_img'] = formato
#         serializer = TablaArchivoSerializer(data=request.data)
#         if serializer.is_valid():
#             validated_data = serializer.validated_data
#             # Guardar el modelo
#             img = TablaArchivo(**validated_data)
#             img.url_img =  'http://localhost:8000/assets/img/' + str(img.url_img)
#             img.save()
#             serializer_response = TablaArchivoSerializer(img)
#             return Response(serializer_response.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# class loadImageTableDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return TablaArchivo.objects.get(pk = pk)
#         except TablaArchivo.DoesNotExist:
#             return 0

#     def get(self, request,pk, format=None):
#         idResponse = self.get_object(pk)
#         if idResponse != 0:
#             idResponse = TablaArchivoSerializer(idResponse)
#             return Response(idResponse.data, status = status.HTTP_200_OK)
#         return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

#     def put(self, request,pk, format=None):
#         idResponse = self.get_object(pk)
#         archivos = request.data['url_img']
#         #archivos = Path(request.data['url_img'])
#         name, formato = os.path.splitext(archivos.name)
#         request.data['name_img'] = name
#         request.data['format_img'] = formato
#         serializer = TablaArchivoSerializer(idResponse, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             datas = serializer.data
#             return Response(datas, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         imagen = self.get_object(pk)
#         if imagen != 0:
#             imagen.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response("Datos no encontrados",status = status.HTTP_400_BAD_REQUEST) 

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path

#Importaciones de modelos
from loadimage.models import TablaImages

#Importaciones de serializadores
from loadimage.serializers import TablaSerializerImg

#Importacion JSON
import json

# Create your views here.


class TablaListImg(APIView):

    def get(self, request, format=None):
        queryset = TablaImages.objects.all()
        serializer = TablaSerializerImg(queryset, many = True, context = {'request':request})
        responseOk = self.responseCustom(serializer.data, "success", status.HTTP_200_OK)
        return Response(responseOk)

    def post(self, request, format=None):
        if 'image' not in request.data:
                raise exceptions.ParseError("Ningun archivo seleccionado") 
        file = request.data['image']
        nombre, formato = os.path.splitext(file.name)
        urlFinal = ''.join(nombre+formato)
        urlFinal = 'http://localhost:8000/assets/img/' + urlFinal
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        request.data['url_img'] = urlFinal
        serializer = TablaSerializerImg(data=request.data)   
        if serializer.is_valid():
            validated_data = serializer.validated_data
            image = TablaImages(**validated_data)
            image.save()
            serializeResponse = TablaSerializerImg(image)
            data = serializeResponse.data
            responseOk = self.responseCustom(data, "success", status.HTTP_201_CREATED)
            return Response(responseOk)
        responseOk = self.responseCustom(serializer.errors, "error", status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)

    def responseCustom(self, data, respuesta, status):
        responseOk = {"messages": respuesta, "pay_load": data, "status": status}
        return responseOk

class TablaImagesDetail(APIView):
    def get_object(self, pk):
        try:
            print(TablaImages.objects.get(pk = pk))
            return TablaImages.objects.get(pk = pk)
        except TablaImages.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = TablaSerializerImg(idResponse)
            responseOk = self.responseCustom(idResponse.data, "success", status.HTTP_200_OK)
            return Response(responseOk)
        responseOk = self.responseCustom("No hay datos", "error", status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)

    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if 'image' not in request.data:
                raise exceptions.ParseError("Ningun archivo seleccionado") 
        file = request.data['image']
        nombre, formato = os.path.splitext(file.name)
        urlFinal = ''.join(nombre+formato)
        urlFinal = 'http://localhost:8000/assets/img/' + urlFinal
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        request.data['url_img'] = urlFinal
        serializer = TablaSerializerImg(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            responseOk = self.responseCustom(datas, "success", status.HTTP_201_CREATED)
            return Response(responseOk)
        responseOk = self.responseCustom(serializer.errors, "error", status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)

    def delete(self, request, pk):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse.image.delete()
            idResponse.delete()
            responseOk = self.responseCustom("Datos eliminados", "success", status.HTTP_201_CREATED)
            return Response(responseOk)
        responseOk = self.responseCustom(idResponse.errors, "error", status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)

    def responseCustom(self, data, respuesta, status):
        responseOk = {"messages": respuesta, "pay_load": data, "status": status}
        return responseOk 