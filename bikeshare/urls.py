"""bikeshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view

from bicycles.views import BicycleViewSet
from users.views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'bicycles', BicycleViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    url(r'^graphql$', GraphQLView.as_view(graphiql=True)),
    path('openapi', get_schema_view(
        title="Bikeshare API",
        description="Complete API for Bikeshare app",
        version="0.1.0"
    ), name='openapi-schema'),
]