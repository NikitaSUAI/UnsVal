from rest_framework.serializers import Serializer, ModelSerializer, CharField
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class GetAnswerModelSerializer(Serializer):

    userId = CharField(required=True)
    line = CharField(required=True)


class IssueTokenRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)


class TokenSeriazliser(ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
