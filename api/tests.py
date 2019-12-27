from django.test import TestCase
from .models import User, Friendship
from faker import Faker


class FriendshipTest(TestCase):

    def setUp(self):
        fake = Faker()
        self.user1 = User.objects.create(
            username=fake.name(),
            dob=fake.date()
        )
        self.user2 = User.objects.create(
            username=fake.name(),
            dob=fake.date()
        )
        self.friendship1 = Friendship.objects.create(
            profile_1=self.user1,
            profile_2=self.user2
        )
        self.friendship2 = Friendship.objects.create(
            profile_1=self.user2,
            profile_2=self.user1
        )
        return self.user1, self.user2, self.friendship1, self.friendship2

    def test_friendship_creation(self):
        u1, u2, f1, f2 = self.setUp()
        self.assertTrue(isinstance(u1, User))
        self.assertTrue(isinstance(u2, User))
        self.assertTrue(isinstance(f1, Friendship))
        self.assertTrue(isinstance(f2, Friendship))
        self.assertEqual(u1.__str__(), u1.name)
        self.assertEqual(u1.__str__(), u2.name)

    def test_friend_of_friend_works(self):
        u1, u2, f1, f2 = self.setUp()
        fof1 = u1.friend_of_friends().values_list('user_id', flat=True)
        fof2 = u2.friend_of_friends().values_list('user_id', flat=True)
        self.assertEqual(u1 not in fof2, u2 not in fof1)
