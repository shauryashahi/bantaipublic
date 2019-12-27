from django.core.management.base import BaseCommand
import random
from faker import Faker
from ...models import User, Friendship
import itertools
import uuid

# python manage.py seed --mode=refresh

# Clear all data and create objects
MODE_REFRESH = 'refresh'

# Clear all data and do not create any object
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = 'seed database for testing and development.'

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help='Mode')

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    # Deletes all the table data
    User.objects.all().delete()
    Friendship.objects.all().delete()


def create_users():
    # Creates 1000 user object
    fake = Faker()
    users = [
        User(
            user_id=uuid.uuid4(),
            username=fake.user_name()+str(uuid.uuid4()),
            name=fake.name(),
            dob=fake.date(),
            gender='M',
            location=fake.city(),
            pic_url=fake.url(),
        )
        for i in range(1000)
    ]
    User.objects.bulk_create(users)


def create_friendships():
    # 1000 users with 50 friendships each = 50000 friendships
    users = User.objects.all()
    all_possible_friendships = [
        Friendship(
            profile_1=friend1,
            profile_2=friend2,
        )
        for friend1, friend2 in
        itertools.combinations(users, 2)
    ]
    random.shuffle(all_possible_friendships)
    friendships = all_possible_friendships[:50000]
    Friendship.objects.bulk_create(friendships)


def run_seed(self, mode):
    # param mode: refresh / clear
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_users()
    create_friendships()
