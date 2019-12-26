from django.core.management.base import BaseCommand
import random
from faker import Faker
from ...models import *
from random import randint
from multiprocessing import Pool

# python manage.py seed --mode=refresh

# Clear all data and creates addresses
MODE_REFRESH = 'refresh'

# Clear all data and do not create any object
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def clear_data():
    #Deletes all the table data
    User.objects.all().delete()
    Friendship.objects.all().delete()


def create_users():
    #Creates 100 user object
    for i in range(0,100):
        print("Creating a user")
        fake = Faker()
        user = User(username=fake.user_name(),name=fake.name(), dob=fake.date(),gender="M",location=fake.city(),pic_url=fake.url())
        try:
            user.save()
        except:
            pass
        print("{} created.".format(user.username))

def create_friendships():
    #Creates a friendship object
    for i in range(0,1000):
        fake = Faker()
        users = User.objects.all()
        count = users.count()
        random_index = randint(0, count - 1)
        random_profile_1 = users[random_index]
        random_index = randint(0, count - 1)
        random_profile_2 = users[random_index]
        user_ids = User.objects.values_list('id', flat=True)
        friendship = Friendship(profile_1=random_profile_1,profile_2=random_profile_2)
        try:
            friendship.save()
        except:
            pass
        print("{} and {} are friends now.".format(friendship.profile_1,friendship.profile_2))

def run_seed(self, mode):
    #param mode: refresh / clear
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return
    processes = (0,1,2,3,4,5) 
    pool = Pool(processes=3)
    pool.map(run_process, processes)

def run_process(process):
    create_users()
    create_friendships()
