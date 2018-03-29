from django.urls import path, include
from api import views
itemList = {"get": "list"}
itemDetail = {"get": "retrieve", "post": "create", "put": "update", "patch": "partial_update", "delete": "destroy"}
urlpatterns=[
    # Lists
    path('units/', views.UnitsViewSet.as_view(itemList), name="units-list"),
    path('locals/', views.LocalsViewSet.as_view(itemList), name="locals-list"),
    path('sensors/', views.SensorsViewSet.as_view(itemList), name="sensors-list"),
    path('alerts/', views.AlertsViewSet.as_view(itemList), name="alerts-list"),
    path('colectors', views.ColectorsViewSet.as_view(itemList), name="colectors-list"),
    # Detailed routes
    path('units/<int:pk>/', views.UnitsViewSet.as_view(itemDetail), name="units-detail"),
    path('locals/<int:pk>/', views.LocalsViewSet.as_view(itemDetail), name="locals-detail"),
    path('sensors/<int:pk>/', views.SensorsViewSet.as_view(itemDetail), name="sensors-detail"),
    path('alerts/<int:pk>/', views.AlertsViewSet.as_view(itemDetail), name="alerts-detail"),
    path('colectors/<int:pk>/', views.ColectorsViewSet.as_view(itemDetail), name="colectors-detail"),
    # Sensors measurements
    path('sensors/<int:idsensor>/measurements/', views.SensorMeasureViewSet.as_view(itemList), name="measurements-list"),
    path('sensors/<int:idsensor>/measurements/<int:pk>/', views.SensorMeasureViewSet.as_view(itemDetail), name="measurements-detail"),
]