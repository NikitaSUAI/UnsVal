from rest_framework import status
from drf_yasg import openapi
from core.serializers import IssueTokenRequestSerializer, GetAnswerModelSerializer, UserSerializer

# 200_EXAPMLE
# {
#     "history": [
#         {
#             "question": "ffsfdsfds",
#             "answer": "new_answer"
#         }
#     ],
#     "key": "fefaa43c053605b8299aedf5defbfe8f6e241c6c"
# }
STATUS_200_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'key': openapi.Schema(type=openapi.TYPE_STRING, description='Auth Token'),
        'userId': openapi.Schema(type=openapi.TYPE_STRING, description='user idetificator'),
        'history': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'question': openapi.Schema(type=openapi.TYPE_STRING, description='Question from user'),
                    'answer': openapi.Schema(type=openapi.TYPE_STRING, description='Answer from model'),
                },
            ),
            description='Dialogs history with user'),
    }
)

LOG_IN_SCHEME = {
    'method': 'post',
    'query_serializer': IssueTokenRequestSerializer,
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Name or login of user'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        },
        required=['username', 'password']
    ),
    'responses': {
        status.HTTP_200_OK: STATUS_200_SCHEMA,
        status.HTTP_400_BAD_REQUEST: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate name or login of user'),
                'password': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate user password'),
            },
        ),
    }
}


GET_ANSWER_SHEME = {
    'method': 'GET',
    'query_serializer': GetAnswerModelSerializer,
    'responses': {
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'answer': openapi.Schema(type=openapi.TYPE_STRING, description='New Answer'),
            }
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'line': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate user request to chatbot'),
                'userId': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate user identificator'),
            },
        ),
    }
}


REGISTRATION_SCHEME = {
    'method': 'post',
    'query_serializer': UserSerializer,
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Name or login of user'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
        },
        required=['username', 'password', 'email']
    ),
    'responses': {
        status.HTTP_200_OK: STATUS_200_SCHEMA,
        status.HTTP_400_BAD_REQUEST: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate name or login of user'),
                'email': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate user email'),
                'password': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING, description='Errors while validate user password'),
            },
        ),
    }
}
