from django.contrib import admin
from .models import userregistertable
# Register your models here.

class showuserregistertable(admin.ModelAdmin):
    list_display = ['email','fname','lname','uspass','uscpass','phone','address']

admin.site.register(userregistertable,showuserregistertable)
