from crudapp2.models import ShivamBytes
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShivamBytes
        fields = ['id', 'name', 'city']