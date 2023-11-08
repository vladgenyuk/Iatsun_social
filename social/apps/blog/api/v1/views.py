import jwt
from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PublicationSerializer
from apps.blog.models import Publication
from social.jwt_decoder import jwt_decode

class MyPublications(APIView):

    def get(self, request, publisher_id: int):
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
        token = request.headers.get('Authorization')
        user = jwt_decode(token)

        data = request.data.copy()
        data['publisher.id'] = str(user.get('user_id'))
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response({'info': 'Publication created',
                             'details': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk: int = None, partial=None, *args, **kwargs):
        publication = get_object_or_404(self.queryset, pk=pk)
        token = request.headers.get('Authorization')
        user = jwt_decode(token)

        if user.get('user_id') != publication.publisher_id:
            return Response({'detail': 'The user ID does not match the publication author ID'}, status=403)

        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(publication, request.data)
            return Response({"info": "Publication updated",
                             "detail": serializer.data
                             }, status=201)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk: int = None, *args, **kwargs):
        publication = get_object_or_404(self.queryset, pk=pk)
        token = request.headers.get('Authorization')
        user = jwt_decode(token)

        if user.get('user_id') != publication.publisher_id:
            return Response({'detail': 'The user ID does not match the publication author ID'}, status=403)

        self.perform_destroy(publication)
        return Response({'info': 'Publication deleted',
                         'detail': 'success',
                         }, status=204)
