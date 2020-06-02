from rest_framework import generics, mixins, permissions
from rest_framework.authentication import  SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NgoSerializer, NgoNameSerializer
from status.models import NGO


class NgoList(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = NgoSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        print(request.user)
        qs =NGO.objects.all()
        query =request.GET.get('q')
        if query is not None:
            qs=qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)

class NgoNameList(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = NgoNameSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        print(request.user)
        qs =NGO.objects.all()
        query =request.GET.get('q')
        if query is not None:
            qs=qs.filter(content__icontains=query)
        return qs

class NgoDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    queryset = NGO.objects.all()
    serializer_class = NgoSerializer
    lookup_field = 'NGO_id'


    def put(self, request, *args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args,**kwargs):
        return self.destroy(request, *args, **kwargs)


