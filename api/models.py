from django.db import models
import uuid
from django.conf import settings


def generate_user_id():
    return str(uuid.uuid4())


class User(models.Model):
    username = models.TextField(unique=True)
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=60, blank=True)
    dob = models.DateField(blank=True)
    gender = models.CharField(
        max_length=20,
        choices=settings.GENDER_CHOICES, blank=True
    )
    location = models.TextField(max_length=60, blank=True)
    pic_url = models.TextField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if len(self.user_id.strip(" ")) == 0:
            self.user_id = generate_user_id()
        super(User, self).save(*args, **kwargs)

    def friend_of_friends(self):
        friend_ids = self.friends.all().values_list('id', flat=True)
        friend_of_friends_ids = Friendship.objects.filter(
            profile_1_id__in=friend_ids
        ).values_list('profile_2_id', flat=True)
        friend_of_friends = User.objects.filter(
            id__in=friend_of_friends_ids
            ).exclude(
                user_id=self.user_id
            )
        return self.order_by_mutual_friends(friend_of_friends)

    def order_by_mutual_friends(self, suggestions):
        suggestions_with_mutual_count = [(
            potential_friend,
            len(
                set(potential_friend.friends.all()
                    .values_list('id', flat=True)) &
                set(self.friends.all().values_list('id', flat=True))
            )
        ) for potential_friend in suggestions]
        improved_suggestions = sorted(
            suggestions_with_mutual_count,
            key=lambda x: x[1],
            reverse=True
        )
        return [suggestion
                for suggestion, mutual_count
                in improved_suggestions]

    class Meta:
        ordering = ['-created_at']


class Friendship(models.Model):
    profile_1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='sender'
    )
    profile_2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='receiver'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} is friends with {}'.format(self.profile_1, self.profile_2)

    class Meta:
        unique_together = ('profile_1', 'profile_2')


User.add_to_class(
    'friends',
    models.ManyToManyField('self', through=Friendship, symmetrical=True)
)
