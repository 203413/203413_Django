# from dataclasses import fields
# from rest_framework import routers, serializers, viewsets

# # importacion de modelos
# from loadimage.models import TablaArchivo

# class TablaArchivoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TablaArchivo
#         fields = ('pk','name_img','format_img', 'url_img')

from rest_framework import routers, serializers, viewsets

#Importancion de modelos
from loadimage.models import TablaImages

class TablaSerializerImg(serializers.ModelSerializer):
    class Meta:
        model = TablaImages
        fields = ("id", "name_img", "url_img", "format_img", "image")