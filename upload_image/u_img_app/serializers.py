from .models import *
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id_user = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True, max_length=60)
    username = serializers.CharField(required=True, max_length=50)
    name = serializers.CharField(required=True, max_length=50)
    surname = serializers.CharField(required=True, max_length=50)
    account_tiers = serializers.CharField(max_length=2, required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.account_tiers = validated_data.get('account_tiers', instance.account_tiers)
        instance.save()
        return instance


class ImageSerializer(serializers.Serializer):
    id_image = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(required=True)
    title = serializers.CharField(required=False, max_length=100, default='')
    url = serializers.URLField(required=True, max_length=200)
    image = serializers.ImageField(required=False)
    format = serializers.CharField(required=True, max_length=1)
    
    # foreign key
    user = serializers.IntegerField(source='user.id_user')

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.image = validated_data.get('image', instance.image)
        instance.format = validated_data.get('format', instance.format)
        instance.save()
        return instance