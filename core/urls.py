"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    Sensor1,
    Sensor2,
    Sensor3,
    Sensor4,
    Usuario,
    login_view,
    login_view2,
    logout_view,
    home_view,
    find_user_view,
    logint_view,
    
    #-------------------modulo 1--------------------

    
    #-------------------recepción--------------------
    Lecturas,
    register_view,

)

app_mame = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home_view, name='home'),
    path('login/', login_view, name='logint'),
    path('reconocimiento-facial/', login_view2, name='login'),
    path('registrarse/', register_view, name='register'),
    path('usuario/', Usuario, name='Usuario'),
    
    path('logout/', logout_view, name='logout'),
    path('classify/', find_user_view, name='classify'),

    #-------------------modulo 1--------------------
    path ('Lecturas/', Lecturas, name='programacionC'),
    path ('Sensor1/', Sensor1, name='Sensor1'),
    path ('Sensor2/', Sensor2, name='Sensor2'),
    path ('Sensor3/', Sensor3, name='Sensor3'),
    path ('Sensor4/', Sensor4, name='Sensor4'),
     
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
