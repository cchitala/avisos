from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1.0/', include('avisos.urls')),
]
