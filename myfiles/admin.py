from django.contrib import admin
from myfiles.models import *
# Register your models here.


class AdminP(admin.ModelAdmin):
    list_display = ['id','nomi','tur','rasm']


admin.site.register(Portfolio,AdminP)



class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']


admin.site.register(Type,AdminType)


class AdminTEAM(admin.ModelAdmin):
    list_display = ['Ism','martaba','rasmi','Instagram','Twiter','Facebok','Linced']


admin.site.register(Team,AdminTEAM)





class AdminM(admin.ModelAdmin):
    list_display = ['id','name','mail','subject','time']

admin.site.register(Message,AdminM)