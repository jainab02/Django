from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 50)
    roll = serializers.IntegerField()
    city =serializers.CharField(max_length = 50)

    def create(self, validated_data):
        return super().create(**validated_data)