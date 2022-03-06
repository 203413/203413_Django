from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from UserProfile.views import TablaProfileList
from UserProfile.views import TablaProfileDetail


urlpatterns = [
    re_path(r'^profile$', TablaProfileList.as_view()),
    re_path(r'^profile/(?P<pk>\d+)$', TablaProfileDetail.as_view()),
]