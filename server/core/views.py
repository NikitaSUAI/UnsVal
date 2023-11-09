from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from core.serializers import UserSerializer, IssueTokenRequestSerializer, TokenSeriazliser
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound

from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth.models import User


@api_view(['POST'])
@require_http_methods(["POST"])
@permission_classes([AllowAny])
def issue_token(request: Request) -> Response:
    serializer = IssueTokenRequestSerializer(data=request.data)
    if serializer.is_valid():
        authenticated_user = authenticate(**serializer.validated_data)
        try:
            token = Token.objects.get(user=authenticated_user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=authenticated_user)

        return Response(TokenSeriazliser(token).data)

    else:
        return Response(serializer.errors, status=400)


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def user(request: Request) -> Response:
    return Response({
        'data': UserSerializer(request.user).data
    })


@permission_classes([IsAuthenticated])
@require_http_methods(["GET"])
def get_answer(request: Request) -> Response:
    """
    Get answer from model
    """

    if request.method != 'GET':
        raise NotFound('Endpoint does not exists')

    return Response({'foo': 'bar'})


@require_http_methods(["POST"])
def create_user(request: Request) -> Response:
    """
    Create new user
    """

    if request.method != 'POST':
        raise NotFound('Endpoint does not exists')

    username: str | None = request.POST.get("username", None)
    email: str | None = request.POST.get("email", None)
    password: str | None = request.POST.get("password", None)

    if None in (username, password):
        raise Exception('Username or Password is empty')

    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        user = authenticate(username=username, password=password)
        login(request, user)

    except Exception:
        raise Exception('Can not sign up user')

    messages.success(request, 'The post has been created successfully.')
    return Response({'success': True})
