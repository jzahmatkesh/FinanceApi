from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ReadOnlyField
from rest_framework.views import set_rollback
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


class ArtyklSerializer(serializers.ModelSerializer):
    kol_name = serializers.CharField(source="kol.name", read_only=True)
    moin_name = serializers.CharField(source="moin.name", read_only=True)
    taf1_name = serializers.CharField(source="taf1.name", read_only=True)
    taf2_name = serializers.CharField(source="taf2.name", read_only=True)
    taf3_name = serializers.CharField(source="taf3.name", read_only=True)

    class Meta:
        model = Artykl
        fields = (
            'sanad',
            'id',
            'kol',
            'kol_name',
            'moin',
            'moin_name',
            'taf1',
            'taf1_name',
            'taf2',
            'taf2_name',
            'taf3',
            'taf3_name',
            'bed',
            'bes',
            'note',
            'user',
            'date_created'
        )


class SanadSerializer(serializers.ModelSerializer):
    artykls = ArtyklSerializer(many=True)
    # id = serializers.IntegerField()
    # date = serializers.CharField()
    # bed = serializers.FloatField()
    # bes = serializers.FloatField()
    # note = serializers.CharField()
    # date_created = serializers.CharField()

    class Meta:
        fields = (
            'id',
            'date',
            # 'bed',
            # 'bes',
            'note',
            'date_created',
            'artykls'
        )
        model = Sanad
