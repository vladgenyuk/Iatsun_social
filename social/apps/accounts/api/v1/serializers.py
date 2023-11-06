from django.contrib.auth import get_user_model

from djoser import serializers as djoser_serializers
from rest_framework import serializers

from apps.accounts.models import get_default_image

User = get_user_model()


class MyUserCreateSerializer(djoser_serializers.UserCreateSerializer):
    photo = serializers.ImageField(write_only=True, required=False)

    class Meta(djoser_serializers.UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'photo', 'email', 'first_name', 'last_name', 'password')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', )
        instance.last_name = validated_data.get('last_name', )
        instance.photo = validated_data.get('photo', ) or get_default_image()
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    photo = serializers.ImageField(read_only=True)
