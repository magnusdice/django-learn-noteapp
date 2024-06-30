from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
        extra_kwargs = {"password":{"write_only": True}}
    
    #method that will called to create a new user, it will look at this model. it will make sure that it is valid
    def create(self,validated_date):
        user = User.objects.create_user(**validated_data)
        return user
        