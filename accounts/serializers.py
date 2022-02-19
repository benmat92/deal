from rest_framework import serializers

from accounts.models import CustomUser
from catalog.models import Deal


class UserSerializer(serializers.HyperlinkedModelSerializer):
    deals = serializers.HyperlinkedRelatedField(many=True, view_name='deal-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
