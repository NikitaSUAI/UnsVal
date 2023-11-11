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
from core.models import Dialogs


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
        username = val_data.get('username')
        password = val_data.get('password')

        try:
            user_id = User.objects.filter(
                username=username)[0].id
        except Exception as e:
            user_id = None
            raise Exception('User does not exists!')

        history = list(Dialogs.objects.filter(
            user_id=user_id).order_by('created_at').values('question', 'answer'))

        token = get_token(username=username,
                          password=password)

        return Response({'history': history, **token, 'userId': user_id})

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

    if request.method != 'GET':
        raise NotFound('Endpoint does not exists')

    serializer = GetAnswerModelSerializer(data=request.query_params)
    if serializer.is_valid():
        pass
        val_data = serializer.validated_data
        line = val_data.get('line')
        userId = val_data.get('userId')
        # -------------псевдо код-----------
        # new_answer = model.get_answer(line)
        # ----------------------------------
        add_dialogs = Dialogs(
            user_id=userId, question=line, answer='new_answer')
        add_dialogs.save()
        # return Response({'answer': new_answer})
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

        try:
            user_id = User.objects.filter(
                username=username)[0].id
        except Exception as e:
            user_id = None
            raise Exception('User does not exists!')

        history = list(Dialogs.objects.filter(
            user_id=user_id).order_by('created_at').values('question', 'answer'))

        token = get_token(username=username,
                          password=password)

        return Response({'history': history, **token, 'userId': user_id})

    else:
        return Response(serializer.errors, status=400)
