from django.contrib import admin
from .models import Person, Tweet


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'birth', 'is_active')


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'message', 'created_at', 'modified_at')
# admin.site.register(Person, PersonAdmin) #usamos el decorador @admin.register()
