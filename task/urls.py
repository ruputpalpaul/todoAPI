from django.urls.conf import re_path
from task.views import TaskViewSet
from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns =[
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('usertask/', UserTaskList.as_view()),
    # path('api/description/<int: id>', TaskViewDescription.as_view())
]