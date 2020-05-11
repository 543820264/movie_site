from django.contrib import admin
from .models import List_1, List_2,Movies


# Register your models here.
@admin.register(List_1)
class List_1Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'created', 'updated']


@admin.register(List_2)
class List_2Admin(admin.ModelAdmin):
    list_display = ['id', 'parent_id', 'name', 'url', 'created', 'updated']


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'column_id', 'column', 'title', 'url_1', 'url_2', 'created', 'updated']


