from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import CustomUser

class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            if user and check_password(password, user.password):
                return user
            
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
