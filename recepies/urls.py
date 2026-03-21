"""
URL configuration for recepies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from vege.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include("vege.urls")),
    path('delete-receipe/<id>/', delete_receipe, name='delete receipe'), 
    path('update-receipe/<id>/', update_receipe, name='update receipe'), 

    path('login/', login_page, name='login page'),
    path('register/', register_page, name='register page'),
    path('logout/',  logout_page, name=' logout page '),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
