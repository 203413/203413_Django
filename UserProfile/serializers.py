from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from UserProfile.models import TablaProfile

class TablaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaProfile
        fields = ('pk','id_user','url_image')