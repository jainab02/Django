# from rest_framework import serializers
# from .models import CustomUser, Contact, SpamReport

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('name', 'phone_number', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ('name', 'phone_number', 'spam_likelihood')

# class SpamReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpamReport
#         fields = ('phone_number', 'count')
from rest_framework import serializers
from .models import Contact,MapUserContact,Profile
from django.contrib.auth.models import User

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
