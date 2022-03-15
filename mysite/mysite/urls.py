from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('simpleapp/', include('simpleapp.urls')),
    path('admin/', admin.site.urls),
    path('oidc/', include('mozilla_django_oidc.urls')),
]
