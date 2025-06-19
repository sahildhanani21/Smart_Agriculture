from django.contrib import admin
from .models import adminlogin
from .models import admindata
from  .models import complaint
# Register your models here.

class showadminlogindetails(admin.ModelAdmin):
    list_display = ['username','password']

class showadmindetails(admin.ModelAdmin):
    list_display = ['email','password']

class showcomplaint(admin.ModelAdmin):
    list_display =['fname','lname','number','email','subject']

admin.site.register(admindata,showadmindetails)
admin.site.register(adminlogin,showadminlogindetails)
admin.site.register(complaint,showcomplaint)
