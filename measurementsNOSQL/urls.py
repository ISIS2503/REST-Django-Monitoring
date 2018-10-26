from django.conf.urls import url, include

from .views import measurementList, measurementDetail


urlpatterns = [
    url('', measurementList),
    url(r'(?P<pk>[0-9]+)$/', measurementDetail),
]