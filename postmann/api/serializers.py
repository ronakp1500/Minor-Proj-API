from rest_framework import serializers
from .models import UsersAPI 

class UsersAPISerializer(serializers.Serializer):
    Name=serializers.CharField(max_length=50)
    Email=serializers.CharField()
    Password=serializers.CharField()

    def create(self,validated_data):
        return UsersAPI.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.Password = validated_data.get('Password', instance.Password)

        instance.save()
        return instance
