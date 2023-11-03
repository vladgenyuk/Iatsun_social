from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import v1

router = DefaultRouter()


urlpatterns = [
    path('', v1, name='v1'),
]

urlpatterns += router.urls
