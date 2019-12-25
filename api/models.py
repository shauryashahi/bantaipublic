from django.db import models

class User(models.Model):
    username = models.TextField(unique=True)
    name = models.CharField(max_length=60)
    dob = models.DateField()
    gender = models.TextChoices('Gender', 'Male Female Transgender')
    location = models.TextField(max_length=60)
    pic_url = models.TextField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

# class Friendship(models.Model):
#     sender_id = models.TextField(db_index = True)
#     receiver_id = models.TextField(db_index = True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name



#           create_table "friendships", primary_key: "false", force: :cascade do |t|
#
#     t.index ["profile_1_id", "profile_2_id"], name: "index_friendships_on_profile_1_id_and_profile_2_id", unique: true
#     t.index ["profile_1_id"], name: "index_friendships_on_profile_1_id"
#     t.index ["profile_2_id", "profile_1_id"], name: "index_friendships_on_profile_2_id_and_profile_1_id", unique: true
#     t.index ["profile_2_id"], name: "index_friendships_on_profile_2_id"
#   end
#
#   add_foreign_key "friendships", "profiles", column: "profile_1_id"
#   add_foreign_key "friendships", "profiles", column: "profile_2_id"
#   add_foreign_key "interests_profiles", "interests"
#   add_foreign_key "interests_profiles", "profiles"
# end
