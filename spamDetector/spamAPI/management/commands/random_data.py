import random
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from spamAPI.models import Contact, MapUserContact, Profile

fake = Faker()

class Command(BaseCommand):
    help = 'Populate database with random data'

    def handle(self, *args, **kwargs):
        num_users = 10
        num_contacts = 20

        users = self.create_fake_users(num_users)
        contacts = self.create_fake_contacts(num_contacts)

        self.create_fake_profiles(users)
        self.map_users_with_contacts(users, contacts)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with random data'))

    def create_fake_users(self, n):
        users = []
        for _ in range(n):
            username = fake.user_name()
            email = fake.email()
            password = 'password123'  # You can use any default password here
            user = User.objects.create_user(username=username, email=email, password=password)
            users.append(user)
        return users

    def create_fake_contacts(self, n):
        contacts = []
        for _ in range(n):
            name = fake.name()
            phone_number = fake.phone_number()
            email = fake.email()
            spam = random.choice([True, False])
            contact = Contact.objects.create(name=name, phone_number=phone_number, email=email, spam=spam)
            contacts.append(contact)
        return contacts

    def create_fake_profiles(self, users):
        for user in users:
            phone_number = fake.phone_number()
            email = fake.email()
            spam = random.choice([True, False])
            profile = Profile.objects.create(user=user, phone_number=phone_number, email=email, spam=spam)

    def map_users_with_contacts(self, users, contacts):
        for user in users:
            # Choose random contacts to map with users
            contacts_to_map = random.sample(contacts, random.randint(1, 5))
            for contact in contacts_to_map:
                MapUserContact.objects.create(user=user, contact=contact)
