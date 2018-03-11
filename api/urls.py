from django.conf.urls import url
from api import views


urlpatterns={
    url(r'^/login'),
    url(r'^/unidades/$', views.units_list),
    url(r'^/locals/$', views.locals_list),
    url(r'^/sensors/$', views.sensors_list),
    url(r'^/alerts/$', views.alerts_list)
}