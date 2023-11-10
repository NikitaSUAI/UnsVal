from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.serializers import IssueTokenRequestSerializer, UserSerializer, GetAnswerModelSerializer
from rest_framework.exceptions import NotFound
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from core.utils import get_token
from core.swagger_schema import LOG_IN_SCHEME, GET_ANSWER_SHEME, REGISTRATION_SCHEME


@swagger_auto_schema(**LOG_IN_SCHEME)
@api_view(['POST'])
@require_http_methods(["POST"])
@permission_classes([AllowAny])
def log_in(request: Request) -> Response:
    """
    User login
    """
    serializer = IssueTokenRequestSerializer(data=request.data)
    if serializer.is_valid():
        val_data = serializer.validated_data

        return get_token(username=val_data.get('username'),
                         password=val_data.get('password'))

    else:
        return Response(serializer.errors, status=400)


@swagger_auto_schema(**GET_ANSWER_SHEME)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@require_http_methods(["GET"])
def get_answer(request: Request) -> Response:
    """
    Get answer from model
    """
    # line = None
    # userId = None

    if request.method != 'GET':
        raise NotFound('Endpoint does not exists')

    serializer = GetAnswerModelSerializer(data=request.data)
    if serializer.is_valid():
        pass
        # val_data = serializer.validated_data
        # line = val_data.get('line')
        # userId = val_data.get('userId')
    else:
        return Response(serializer.errors, status=400)

    return Response({'answer': 'new_answer'})


@swagger_auto_schema(**REGISTRATION_SCHEME)
@api_view(['POST'])
@require_http_methods(["POST"])
def registration(request: Request) -> Response:
    """
    Create new user
    """

    if request.method != 'POST':
        raise NotFound('Endpoint does not exists')

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():

        # try:
        val_data = serializer.validated_data
        username = val_data.get('username')
        password = val_data.get('password')

        user = User.objects.create_user(
            username=username,
            email=val_data.get('email'),
            password=password
        )

        user.save()

    else:
        return Response(serializer.errors, status=400)

    return get_token(username=val_data.get('username'),
                     password=val_data.get('password'))
