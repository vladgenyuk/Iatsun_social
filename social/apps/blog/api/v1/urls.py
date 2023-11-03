from rest_framework.routers import DefaultRouter

from .views import PublicationViewSet

router = DefaultRouter()
router.register(r'Publication', PublicationViewSet, basename='Publication')

urlpatterns = [

]

urlpatterns += router.urls
