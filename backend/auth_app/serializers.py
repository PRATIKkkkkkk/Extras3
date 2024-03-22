from rest_framework import serializers
from django.contrib.auth import get_user_model
from app1.serializers import StudentSerializer

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    names = StudentSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'names')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)