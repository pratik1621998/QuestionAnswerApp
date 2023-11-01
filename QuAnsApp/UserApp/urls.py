from django.contrib import admin
from django.urls import  path

from UserApp.views import *

urlpatterns = [

    #------------------------------ REGISTRATION ----------------------------# 

    path('user-register', UserRegisterAPI.as_view(), name= "UserRegisterAPI"),
    path('register', registration_form_view, name= "registration"),

    path('user-login', LoginUserAPI.as_view(), name= "LoginUserAPI"),
    path('login', login_form_view, name= "login"),
    # path('user-logout', LogoutAPI.as_view(), name= "LogoutUserAPI"),

    path('main-page', main_page_view, name= "main_page"),

    path('user-profile', GetProfileAPI.as_view(), name= "GetProfileAPI"),

    path('ask-question', QuestionsAPI.as_view(), name= "AddQuestionsAPI"),
    path('all-questions', QuestionsAPI.as_view(), name= "AllQuestionsAPI"),


    path('give-answer', AnswerAPI.as_view(), name= "AddAnswerAPI"),

    path('all-answers', GetAllAnswer.as_view(), name= "AllAnswerAPI"),

    path('like-answer', LikeAnswersAPI.as_view(), name= "LikeAnswerAPI"),

]