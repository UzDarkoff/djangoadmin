from django.contrib import admin
from .models import *
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','phone_number', 'email')
    list_display_links = ['full_name']
    search_fields = ['full_name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title','start_time','end_time')
    list_display_links = ['title']
    search_fields = ['title']
admin.site.register(Student, StudentsAdmin)
admin.site.register(Course, CourseAdmin)

# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id','title','context')
#     list_display_links = ['title']
#     search_fields = ['title']


# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ('id','title')
#     list_display_links = ['title']
#     search_fields = ['title']
# admin.site.register(News,NewsAdmin)
# admin.site.register(Categories,CategoriesAdmin)