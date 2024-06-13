from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=10, null=False)  # Changed to CharField with max_length 10
    email = models.EmailField(max_length=50, null=True)
    spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MapUserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.user) + "," + str(self.contact)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    phone_number = models.CharField(max_length=10, null=False, unique=True)  # Changed to CharField with max_length 10
    email = models.EmailField(max_length=50, null=True)
    spam = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


# class CustomUser(models.Model):
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20, unique=True)
#     email = models.CharField(max_length=255, blank=True)
#     password = models.CharField(max_length=128)

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)

# # class CustomToken(Token):
# #     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='auth_token')

# class Contact(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)

# class SpamReport(models.Model):
#     phone_number = models.CharField(max_length=20)
#     count = models.IntegerField(default=0)

# # Define a one-to-one relationship between CustomUser and Token
# Token._meta.get_field('user').related_model = CustomUser