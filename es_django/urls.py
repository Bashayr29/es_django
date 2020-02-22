from __future__ import unicode_literals

from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
urlpatterns = [
    url(r'^', include(router.urls)),
]
