from rest_framework import serializers

from accounts.models import CustomUser
from catalog.models import Deal


class UserSerializer(serializers.HyperlinkedModelSerializer):
    deals = serializers.HyperlinkedRelatedField(many=True, view_name='deal-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields='__all__'
