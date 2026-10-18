from django.contrib.auth.models import User
from rest_framework import serializers

from .models import KBEntry


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=6)
    company_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('This username is already taken.')
        return value


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class KBEntrySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = KBEntry
        fields = ['id', 'question', 'answer', 'category']

    def get_id(self, obj):
        return str(obj.id)


class KBQuerySerializer(serializers.Serializer):
    search = serializers.CharField(
        allow_blank=True,
        required=True,
        error_messages={
            'required': 'The "search" field is required and cannot be blank.',
            'blank': 'The "search" field is required and cannot be blank.',
        },
    )

    def validate_search(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError('The "search" field is required and cannot be blank.')
        return value.strip()
