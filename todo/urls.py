from rest_framework import routers

from .views import TodoViewSet

from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(prefix='api/v1/todo', viewset=TodoViewSet, basename='todo')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.render, name='render'),
# ]
