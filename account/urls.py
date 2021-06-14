from .views import AccountViewSet
from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'task', AccountViewSet)


urlpatterns =[
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('register/', RegisterView.as_view(), name='auth_register'),
]