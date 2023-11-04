from django.urls import path, include

urlpatterns = [
    path('v1/Publication/', include('apps.blog.api.v1.urls'))
]
