from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'db_req', views.db_req, name='db_req'),
    url(r'bus_search', views.bus_search, name='bus_search'),
]

