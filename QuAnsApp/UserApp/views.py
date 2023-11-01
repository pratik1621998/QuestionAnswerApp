from UserApp.models import *
from UserApp.serializers import *
from rest_framework.views import APIView
from core.response import *
from django.db.models import Q
import re
from core.authenticate import *
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from rest_framework_simplejwt.tokens import RefreshToken

def registration_form_view(request):
    return render(request, 'register.html')

def login_form_view(request):
    return render(request, 'login.html')

def main_page_view(request):
    return render(request, 'mainScreen.html')
 
#------------------- REGISTRATION -----------------#

class UserRegisterAPI(APIView):
    # renderer_classes = [TemplateHTMLRenderer]

    def post(self, request):
        data = request.data
        if data["username"] != (None or "") and data["email"] != (None or "") and data["password"] != (None or "") and data["password2"] != (None or ""):
            if len(data['username']) > 5:
                if len(data['phone_number']) == 10 and re.match("[6-9][0-9]{9}", data['phone_number']):
                    if data['email'] != "" and re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", data["email"]):  
                        if data["password"] == data["password2"]:
                            existingUser = User.objects.filter(Q(username = data["username"]) | Q(phone_number = data["phone_number"]) | Q(email = data["email"]))
                            if not existingUser:
                                serializer = UserRegistrationSerializer(data=data)
                                if serializer.is_valid():
                                    password = make_password(data['password'])
                                    serializer.save(password=password)
                                    return onSuccess("User created successfully !!!", serializer.data)
                                else:
                                    return badRequest(serializer.errors)
                            else:
                                return badRequest("User already exists with username or email or phone number !!!")
                        else:
                            return badRequest("Password and Confirm password doesn't matched !!!")
                    else:
                        return badRequest("Invalid email id, Please try again. !!!")
                else:
                    return badRequest("Invalid mobile number, Please try again. !!!")
            else:
                return badRequest("Username must be greater than 5 letters")
        else:
            return badRequest("username, email, gender, birth_date and profile_type is required to fill.")


# #------------------------ LOGIN USER -------------------------#

class LoginUserAPI(APIView):
    def post(self, request):

        data = request.data
        if data["login_key"] != (None or "") and data["password"] != (None or ""):
            if (len(data['login_key']) == 10 and re.match("[6-9][0-9]{9}", data['login_key'])) or (re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", data["login_key"])):
                try:
                    getUser = User.objects.filter(Q(phone_number = data["login_key"]) | Q(email = data["login_key"]))
                except:
                    return badRequest("User not found.")
                for i in getUser:
                    password = i.password
                    id = i.id
                if getUser:
                    checkPassword = check_password(data["password"], password) 
                    if checkPassword:
                        token=  create_access_token(id)
                        return onSuccess("Login successful !!!", {"token": token})
                    else:
                        return badRequest("Invalid Credentials.")
                else:
                    return badRequest("User not found.")  
            else:
                return badRequest("Invalid email or password.")
        else:
            return badRequest("email or mobile number and password is required for login.")


# class LogoutAPI(APIView):
#     def post(self, request):
#         token = authenticate(request)
#         # print(token)
#         if token:
#             try:
#                 refresh_token = request.META.get('HTTP_AUTHORIZATION', None)
#                 token = RefreshToken(refresh_token)
#                 token.blacklist()
#                 return onSuccess("Logout Successfully.",1)
#             except Exception as e:
#                 return badRequest("Invalid token.")
#         else:
#             return unauthorisedRequest()


#------------------ ADD INTERESTS --------------#

class QuestionsAPI(APIView):

    def get(self, request):
        token = authenticate(request)
        if token:
            try:
                get_user = User.objects.get(id = token["user_id"])
            except:
                return badRequest("User not found !!!")
            
            question_objs = Question.objects.all()
            if question_objs:
                serializer = AllQuestionSerializer(question_objs, many=True)
                return onSuccess("Questions List !!!",  serializer.data)
            else:
                serializer = AllQuestionSerializer(question_objs, many=True)
                return onSuccess("Questions List !!!",  serializer.data)
        else:
            return unauthorisedRequest()

    def post(self, request):
        token = authenticate(request)
        if token:
            try:
                get_user = User.objects.get(id = token["user_id"])
            except:
                return badRequest("User not found !!!")
            data = request.data
            if data["title"] != ("" or None):
                exisiting_question = Question.objects.filter(title = data["title"])
                if not exisiting_question:
                    data["author"] = get_user.id
                    serializer =  AddQuestionSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return onSuccess("Question Asked successfully.", serializer.data)
                    else:
                        return badRequest(serializer.errors)
                else:
                    return badRequest("Question already asked with same title")
            else:
                return badRequest("Question title is required")
        else:
            return unauthorisedRequest()
        

#----------------------- ANSWERS API ------------------------#

class AnswerAPI(APIView):

    def post(self, request):
        token = authenticate(request)
        if token:
            try:
                get_user = User.objects.get(id = token["user_id"])
            except:
                return badRequest("User not found !!!")
            data = request.data
            if data["content"] != ("" or None) and data["question_id"] != ("" or None):
                try:
                    get_question = Question.objects.get(question_id = data["question_id"])
                except:
                    return badRequest("Question doesn't found.")
                data["author"] = get_user.id
                data["question"] = get_question.question_id
                serializer =  AddAnswerSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return onSuccess("Answer Added successfully.", serializer.data)
                else:
                    return badRequest(serializer.errors)
            else:
                return badRequest("Question and Answer is required")
        else:
            return unauthorisedRequest()
        

#------------------- GET ALL ANSWER -------------------#

class GetAllAnswer(APIView):
    def get(self, request):
        token = authenticate(request)
        if token:
            try:
                get_user = User.objects.get(id = token["user_id"])
            except:
                return badRequest("User not found !!!")
            
            question_objs = Answer.objects.all()
            if question_objs:
                serializer = AllAnswerSerializer(question_objs, many=True)
                return onSuccess("Answers List !!!",  serializer.data)
            else:
                serializer = AllAnswerSerializer(question_objs, many=True)
                return onSuccess("Answers List !!!",  serializer.data)
        else:
            return unauthorisedRequest()

       
#------------------------ LIKE USERS ANSWERS -------------------#

class LikeAnswersAPI(APIView):
    def post(self, request):
        token = authenticate(request)
        if token:
            try:
                get_user = User.objects.get(id = token["user_id"])
            except:
                return badRequest("User not found !!!")
            data = request.data
            if data["answer_id"] != ("" or None):
                try:
                    get_answer = Answer.objects.get(answer_id = data["answer_id"])
                except:
                    return badRequest("Answer doesn't found.")
                get_liked_object = Like.objects.filter(answer = data["answer_id"], user = get_user.id)
                if not get_liked_object.exists():
                    data["user"] = get_user.id
                    data["answer"] = get_answer.answer_id
                    serializer =  LikeAnswerSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return onSuccess("Answer Liked successfully.", serializer.data)
                    else:
                        return badRequest(serializer.errors)
                else:
                    return badRequest("Answer already liked.")
            else:
                return badRequest("Question and Answer is required")
        else:
            return unauthorisedRequest()


# #------------------------ GET USER PROFILE ----------------------#

class GetProfileAPI(APIView):
    def get(self, request):
        token = authenticate(request)
        if token:
            try:
                get_user = User.objects.get(id = token["user_id"])
            except:
                return badRequest("User not found!")
            serializer = UserSerializer(get_user)
            return onSuccess("User Profile !!!", serializer.data)
        else:
            return unauthorisedRequest()       