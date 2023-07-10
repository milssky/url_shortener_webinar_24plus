from rest_framework.fields import SlugField
from rest_framework.serializers import ModelSerializer

from shortener.models import Url
from shortener.utils import get_unique_short_url


class UrlSerializer(ModelSerializer):
    short_url = SlugField(allow_blank=True)
    class Meta:
        model = Url
        fields = "__all__"

    def create(self, validated_data):
        if not validated_data['short_url']:
            validated_data['short_url'] = get_unique_short_url()
        return super().create(validated_data)
    
    
