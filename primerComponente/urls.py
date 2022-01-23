from django import views
from django.urls import URLPattern
from django.urls import path,re_path
from django.conf.urls import include

from primerComponente.views import PrimerTablaList

urlpatterns=[
    re_path(r'^primer_componente/$',PrimerTablaList.as_view())
]