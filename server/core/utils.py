from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from core.serializers import TokenSeriazliser
from rest_framework.response import Response


def get_token(username: str, password: str) -> Response:
    """
    Create or find user auth token
    :username: str 
    :password: str
    """
    authenticated_user = authenticate(username=username, password=password)
    try:
        token = Token.objects.get(user=authenticated_user)
    except Token.DoesNotExist:
        token = Token.objects.create(user=authenticated_user)

    return Response(TokenSeriazliser(token).data)
