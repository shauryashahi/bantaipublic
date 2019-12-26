from django.db import models
import uuid

def generate_user_id():
    return str(uuid.uuid4()).split("-")[-1]

class User(models.Model):
    username = models.TextField(unique=True)
    user_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=60)
    dob = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    location = models.TextField(max_length=60)
    pic_url = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if len(self.user_id.strip(" "))==0:
            self.user_id = generate_user_id()
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

class Friendship(models.Model):
    profile_1 = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True,related_name='sender')
    profile_2 = models.ForeignKey(User, on_delete=models.CASCADE, db_index = True,related_name='receiver')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} is friends with {}'.format(self.profile_1,self.profile_2)

    class Meta:
        unique_together = ('profile_1', 'profile_2')

User.add_to_class('friends', models.ManyToManyField('self',through=Friendship,symmetrical=True))
