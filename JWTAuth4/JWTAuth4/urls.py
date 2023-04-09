"""JWTAuth4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from testapp.views import ApiCheck
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',ApiCheck,basename="api")
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token,refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls),name="api"),
    path('get-api-token/',views.obtain_auth_token,name="get-api-token"),
    path('auth-jwt-token/',obtain_jwt_token,name="jwt-token"),
    path('auth-jwt-verify/',verify_jwt_token,name="verify-token"),
    path('auth-jwt-refresh/',refresh_jwt_token,name="refresh-token")
]
