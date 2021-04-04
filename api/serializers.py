from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Kol, Moin, Tafsili, Sanad, Artykl


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', 'Email is already used'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class KolSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'kind'
        )
        model = Kol


class MoinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'kol',
            'id',
            'name',
            'kind'
        )
        model = Moin


class TafsiliSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name'
        )
        model = Tafsili


class SanadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'date',
            'note',
            'date_created'
        )
        model = Sanad


class ArtyklSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'sanad',
            'id',
            'kol',
            'moin',
            'taf1',
            'taf2',
            'taf3',
            'bed',
            'bes',
            'note',
            'user',
            'date_created'
        )
        model = Artykl
