from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(max_length=200)
    #password = serializers.CharField(max_length=20)

    class Meta:
        model = Users
        fields = ('name','password')
