from django.utils import timezone

from rest_framework import serializers

from apps.accounts.api.v1.serializers import UserSerializer
from apps.blog.models import Publication, get_default_image


class PublicationSerializer(serializers.ModelSerializer):
    publisher = UserSerializer()
    published_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    slug = serializers.SlugField(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Publication
        fields = ['id', 'title', 'image', 'content', 'published_at', 'updated_at', 'slug', 'publisher']

    def create(self, validated_data: dict):
        publication = Publication.objects.create(
            title=validated_data.get('title'),
            content=validated_data.get('content'),
            published_at=timezone.now(),
            publisher_id=validated_data.get('publisher').get('id'),
            image=validated_data.get('image') or get_default_image()
        )
        publication.save()
        return publication

    def update(self, instance, validated_data: dict, pk=None):
        instance.title = validated_data.get('title')
        instance.content = validated_data.get('content')
        instance.image = validated_data.get('image')
        instance.updated_at = timezone.now()
        instance.save()
        return instance
