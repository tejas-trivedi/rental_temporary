from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    serializer_class =UserSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'


    def put(self, request, *args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args,**kwargs):
        return self.destroy(request, *args, **kwargs)