from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Speaker, Conference, Performance


# Register your models here.
@admin.register(Speaker)
class Speaker(admin.ModelAdmin):
    list_display = ['telegram_id', 'fullname']


@admin.register(Conference)
class Conference(admin.ModelAdmin):
    list_display = ['name', 'date']


@admin.register(Performance)
class Performance(admin.ModelAdmin):
    list_display = ['name', 'time', 'speaker', 'conference']
    list_filter = ['conference']


admin.site.unregister(User)
admin.site.unregister(Group)
