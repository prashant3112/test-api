'''from django.urls import path
from .views import UsersViews

urlpatterns = [
    path('Users/', UsersViews.as_view())
]'''

from django.urls import include, path

from rest_framework import routers

from .views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
