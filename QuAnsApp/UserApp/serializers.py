from rest_framework import serializers
from UserApp.models import *

#------------------- USER REGISTRATION SERIALIZER -----------------------#

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

#------------------- USER PROFILE SERIALIZER -----------------------#

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

#------------------- ADD QUESTION -------------------------#

class AddQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = "__all__"

#------------------- ALL QUESTIONS -------------------------#

class AllQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = "__all__"

#------------------- ADD ANSWER -------------------------#

class AddAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = "__all__"

#------------------ ALL ANSWER ------------------------------#

class AllAnswerSerializer(serializers.ModelSerializer):
    question = AllQuestionSerializer()

    class Meta:
        model = Answer
        fields = "__all__"

#------------------ LIKE ANSWER ------------------------------#

class LikeAnswerSerializer(serializers.ModelSerializer):
    # answer = AllAnswerSerializer()
    # user = UserSerializer()
    class Meta:
        model = Like
        fields = "__all__"




