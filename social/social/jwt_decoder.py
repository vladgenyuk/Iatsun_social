import jwt
from django.conf import settings

from rest_framework.response import Response


def jwt_decode(token: str):
    if not token:
        return Response({'info': 'Token was not provided'}, status=401)

    token = token.split(' ')[1]

    user = jwt.decode(token, algorithms=['HS256'], key=settings.SECRET_KEY)
    return user
