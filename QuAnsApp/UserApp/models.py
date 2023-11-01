from django.db import models
import uuid
import datetime

# Create your models here.

class User(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    username = models.CharField(max_length=50, unique= True)
    email = models.EmailField(max_length=255, null=True,unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password =  models.CharField(max_length=255,null=True)
    is_verified = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    user_created_at = models.DateTimeField(default=datetime.datetime.now)
    user_modified_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.full_name}"
    
class Question(models.Model):
    question_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Answer(models.Model):
    answer_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    content = models.TextField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question}"

class Like(models.Model):
    like_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
