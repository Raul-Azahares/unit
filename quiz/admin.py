from django.contrib import admin
from .models import *




class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_filter = ('text',)
    search_fields = ('text',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_filter = ('text',)
    search_fields = ('text',)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)