from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status # http.HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.permissions import HaveSecretWordOrReadOnly
from api.serializers import UrlSerializer
from shortener.models import Url


class UrlViewSet(ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = (HaveSecretWordOrReadOnly,)
    pagination_class = LimitOffsetPagination


class UrlRedirectView(APIView):
    def get(self, request, slug):
        url_obj = get_object_or_404(Url, short_url=slug)
        url_obj.nums_of_visits += 1
        url_obj.save()
        return Response(
            status=status.HTTP_302_FOUND,
            headers={"Location": url_obj.full_url}
        )
