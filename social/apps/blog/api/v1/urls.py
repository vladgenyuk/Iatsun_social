from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PublicationViewSet, MyPublications

router = DefaultRouter()
router.register(r'', PublicationViewSet, basename='Publication')

urlpatterns = [
    path('my/<int:publisher_id>', MyPublications.as_view(), name='My publications'),
]

urlpatterns += router.urls
