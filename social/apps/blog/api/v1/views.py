from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PublicationSerializer
from apps.blog.models import Publication


class MyPublications(APIView):

    def get(self, request, publisher_id: int, format=None):
        my_posts = Publication.objects.filter(publisher_id=publisher_id)
        serializer = PublicationSerializer(my_posts, many=True)
        return Response(serializer.data, status=200)


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    permission_classes = []
    serializer_class = PublicationSerializer

    def retrieve(self, request, pk: int = None, *args, **kwargs):
        publication = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(publication)
        return Response(serializer.data, status=200)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'info': 'Publication created',
                             'details': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk: int = None, partial = None, *args, **kwargs):
        publication = get_object_or_404(self.queryset, pk=pk)
        data = dict(publication.__dict__, **request.data)
        if publication.publisher_id != data.get('publisher').get('id'):
            return Response(status=403)
        serializer = self.serializer_class(data=data, partial=True)
        if serializer.is_valid():
            serializer.update(publication, data)
            return Response({"info": "Publication updated",
                             "detail": serializer.data
                             }, status=201)
        return Response(serializer.errors, status=400)
