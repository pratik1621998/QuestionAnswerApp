from django.contrib import admin
from django.contrib.auth.models import Group
from UserApp.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.unregister(Group)

#----------------- USER ADMIN---------------#

class UserAdmin(BaseUserAdmin):
    list_display = ['id','email','username', 'phone_number']
    list_filter = ['is_verified',]
    list_per_page = 10

    fieldsets = (
        ('User Credentials', {'fields': ('username','email','password')}),
        ('Personal info', {'fields': ('full_name', 'phone_number','user_created_at','user_modified_at')}),
        ('Permissions', {'fields': ('is_verified', 'is_active', 'is_staff')}),
    )
    filter_horizontal = ()
    search_fields = ['email', 'username']
    ordering = ['id']
    readonly_fields = ('user_created_at','user_modified_at',)

admin.site.register(User, UserAdmin)

#----------------------- QUESTION ADMIN ----------------#

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_id','title','author', 'created_at', 'modified_at',]
    list_filter = ('author', )
    search_fields = ('title','question_id',)
    list_editable = []
    readonly_fields = ('created_at','modified_at',)
    ordering = ('question_id',)
    list_per_page = 10

admin.site.register(Question, QuestionAdmin)

#------------------- ANSWER ADMIN --------------------#

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_id','question','author', 'created_at', 'modified_at',]
    list_filter = ('author', )
    search_fields = ('question','question_id',)
    list_editable = []
    readonly_fields = ('created_at','modified_at',)
    ordering = ('answer_id',)
    list_per_page = 10

admin.site.register(Answer, AnswerAdmin)


#------------------- LIKE ADMIN --------------------#

class LikeAdmin(admin.ModelAdmin):
    list_display = ['like_id','answer','user',]
    list_filter = ( )
    search_fields = ('answer',)
    list_editable = []
    readonly_fields = ()
    ordering = ('like_id',)
    list_per_page = 10

admin.site.register(Like, LikeAdmin)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(Like)
