from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact,MapUserContact,Profile
from .serializers import ContactSerializer

class ContactList(APIView):
	def get(self,request):
		contacts=Contact.objects.all()
		serializer=ContactSerializer(contacts,many=True)
		return Response(
			serializer.data
		)
	def post(self,request):
		if request.data["name"] is None or request.data["phone_number"] is None:
			return Response(
				{
					"Error":"Both name and phone_number are required"
				},
				status = status.HTTP_400_BAD_REQUEST
			)
		try:
			if request.data["email"]:
				email=request.data["email"]
		except:
				email=None
		contact=Contact.objects.create(
				name=request.data["name"],
				phone_number=request.data["phone_number"],
				email=email,
			)
		mapping=MapUserContact.objects.create(
				user=request.user,
				contact=contact,
			)
		return Response(
			{
				"Message":"Contact saved successfully!!"
			},
			status = status.HTTP_201_CREATED
		)

@permission_classes((AllowAny,))
class Register(APIView):
	def post(self,request):
		if request.data["name"] is None or request.data["phone_number"] is None:
			return Response(
				{
					"Error":"Both name and phone_number are required"
				}, 
				status = status.HTTP_400_BAD_REQUEST
			)
		try:
			if request.data["email"]:
				email = request.data["email"]
		except:
			email="NONE"
		user=User(
				username=request.data["name"],
				password=request.data["password"],
				email=email,
			)
		if user:
			user.set_password(request.data["password"])
			user.save()
			profile=Profile.objects.create(
	        		user=user,
	        		phone_number=request.data["phone_number"],
	        		email=email,
	        	)
			return Response(
	        	{
	        		"Message":"Registered successfully"
	        	},
	        	status = status.HTTP_200_OK
	        )
		else:
			return Response(
        		{
        			"Message":"Error during Signup!!"
        		},
        		status = status.HTTP_400_BAD_REQUEST
        	)

@permission_classes((AllowAny,))
class Login(APIView):
	def post(self,request):
		if not request.data:
			return Response(
				{
					"Error":"Please provide username/password"
				},
				status=status.HTTP_400_BAD_REQUEST
			)
		username=request.data.get("username")
		password=request.data.get("password")
		if username is None or password is None:
			return Response(
				{
					"Error":"Invalid Credentials"
				},
				status=status.HTTP_404_NOT_FOUND
			)
		user = authenticate(username = username, password = password)
		token, _ =Token.objects.get_or_create(user = user)
		return Response(
			{
				"Token":token.key
			},
			status=status.HTTP_200_OK
		)

class MarkSpam(APIView):
	def post(self,request):
		phone_number=request.data.get("phone_number")
		if request.data["phone_number"] is None:
			return Response(
				{
					"Error":"Phone number required!!"
				},
				status = status.HTTP_400_BAD_REQUEST
			)
		contact=Contact.objects.filter(phone_number=phone_number).update(spam=True)
		profile=Profile.objects.filter(phone_number=phone_number).update(spam=True)
		if (contact+profile):
			return Response(
				{
					"Message":"Contact marked as spam successfully!!"
				},
				status = status.HTTP_200_OK
			)
		else:
			return Response(
				{
					"Error":"Phone number not found!!"
				},
				status = status.HTTP_404_NOT_FOUND
			)


class SearchName(APIView):
	def get(self,request):
		name=request.data.get("name")
		if request.data["name"] is None:
			return Response(
				{
					"Error":"Name is required!!"
				},
				status = status.HTTP_400_BAD_REQUEST
			)
		profile_start=Profile.objects.filter(user__username__startswith=name)
		profile_contain=Profile.objects.filter(user__username__contains=name).exclude(user__username__startswith=name)
		contact_start=Contact.objects.filter(name__startswith=name)
		contact_contain=Contact.objects.filter(name__contains=name).exclude(name__startswith=name)
		response=[]
		for contact in profile_start:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		for contact in contact_start:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		for contact in profile_contain:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		for contact in contact_contain:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		return Response(
				response,
				status=status.HTTP_200_OK
			)

class SearchPhoneNumber(APIView):
	def get(self,request):
		phone_number=request.data.get("phone_number")
		if request.data["phone_number"] is None:
			return Response(
				{
					"Error":"Phone number required!!"
				},
				status = status.HTTP_400_BAD_REQUEST
			)
		profile=Profile.objects.filter(phone_number=phone_number)
		if profile:
			user=User.objects.filter(id=profile.id,is_active=True)
			return Response(
					{
						"name":user.username,
						"phone_number":profile.phone_number,
						"spam":profile.spam,
						"email":profile.email
					}
				)
		else:
			contact=Contact.objects.filter(phone_number=phone_number)
			serializer=ContactSerializer(contact,many=True)
			return Response(
					serializer.data
				)

# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from django.contrib.auth import authenticate
# from .models import *
# from .serializers import UserSerializer, ContactSerializer, SpamReportSerializer
# from rest_framework.authtoken.models import Token
# import re


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # class LoginView(APIView):
# #     print('False')
# #     def post(self, request):
# #         print(request)
# #         phone_number = request.data.get('phone_number')
# #         password = request.data.get('password')
# #         # user = authenticate(phone_number=phone_number, password=password)
# #         print(password)
# #         print(phone_number)
# #         # Authenticate using phone_number and password
# #         user = authenticate(request=request, phone_number=phone_number, password=password)
# #         print(user)
# #         if user is not None:
# #             print('true')
# #             # Authentication successful, generate token
# #             token, created = Token.objects.get_or_create(user=user)
# #             return Response({'token': token.key}, status=status.HTTP_200_OK)
# #         else:
# #             # Authentication failed
# #             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class LoginView(APIView):
#     def post(self, request):
#         phone_number = request.data.get('phone_number')
#         password = request.data.get('password')
#         user = authenticate(request=request, phone_number=phone_number, password=password)
#         print("True")
#         if user is not None and isinstance(user, CustomUser):
#             print(user)
#             token, _  = Token.objects.create(user=user)
#             print(token)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             print("user nnot found")
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

# class MarkSpamView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         phone_number = request.data.get('phone_number')
#         try:
#             report, created = SpamReport.objects.get_or_create(phone_number=phone_number)
#             if created:
#                 report.count = 1
#             else:
#                 report.count += 1
#             report.save()
#             return Response({'message': 'Spam reported successfully'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class SearchByNameView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         query = request.GET.get('query')
#         user = request.user
#         contacts = Contact.objects.filter(user=user, name__iregex=rf"^{query}") | Contact.objects.filter(user__isnull=True, name__iregex=query)
#         results = []
#         for contact in contacts:
#             try:
#                 report = SpamReport.objects.get(phone_number=contact.phone_number)
#                 spam_likelihood = report.count
#             except SpamReport.DoesNotExist:
#                 spam_likelihood = 0
#             serializer = ContactSerializer(contact, data={'spam_likelihood': spam_likelihood})
#             serializer.is_valid(raise_exception=True)
#             results.append(serializer.data)
#         return Response(results, status=status.HTTP_200_OK)


# class SearchByPhoneView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         query = request.GET.get('query')
#         user = request.user
#         if re.fullmatch(r'\d+$', query):  # Check if phone number only contains digits
#             try:
#                 contact = Contact.objects.get(user=user, phone_number=query)
#                 serializer = ContactSerializer(contact)
#                 serializer.is_valid(raise_exception=True)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Contact.DoesNotExist:
#                 pass
#         contacts = Contact.objects.filter(phone_number=query)
#         results = []
#         for contact in contacts:
#             try:
#                 report = SpamReport.objects.get(phone_number=contact.phone_number)
#                 spam_likelihood = report.count
#             except SpamReport.DoesNotExist:
#                 spam_likelihood = 0
#             data = ContactSerializer(contact).data.copy()
#             del data['email']  # Exclude email by default
#             if contact.user == user:  # Include email only for user's contacts
#                 data['email'] = contact.email
#             results.append(data)
#         return Response(results, status=status.HTTP_200_OK)