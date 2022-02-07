from django.urls import path, re_path
from django.conf.urls import include

#Importacion de vistas
from loadimage.views import loadImageTable,loadImageTableDetail

urlpatterns = [
    re_path(r'^form/$', loadImageTable.as_view()),
    re_path(r'^form/(?P<pk>\d+)$', loadImageTableDetail.as_view()),    
] 