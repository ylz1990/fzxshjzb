from django.contrib import admin
from .models import Article,College
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','author',"title","pub_time"]
    list_per_page = 10

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id',"title"]
    list_per_page = 10

admin.site.register(Article,ArticleAdmin)
admin.site.register(College,CollegeAdmin)
