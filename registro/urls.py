from django.urls import path, re_path
from django.conf.urls import include


from registro.views import RegistroView

urlpatterns = [
    re_path(r'^', RegistroView.as_view()),    
]