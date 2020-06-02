from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.timezone import now
from rest_framework import generics, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.conf import settings

User = get_user_model()

class TokenCreateView(utils.ActionViewMixin, generics.GenericAPIView):
    serializer_class = settings.SERIALIZERS.token_create
    permission_classes = settings.PERMISSIONS.token_create

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = settings.SERIALIZERS.token
        data = token_serializer_class(token).data
        return Response(
            data, status=status.HTTP_200_OK
        )
