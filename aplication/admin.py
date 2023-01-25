from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
        list_display = ('cat',) #('image_tag','title','description','url','add_date')
        search_fields=('cat',)

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','user','cat','price','slug','add_date','published','premium','amount','amountselled',] #['image_tag','title','url','cat']
    search_fields=['title',]
    list_filter=('cat',)
    list_per_page=50

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','user','created_at','published','postid',]
    search_fields=['postid',]


class BankAdmin(admin.ModelAdmin):
    list_display = ['user','acctype','balance','releasebalance','accpoints',]

class VerifiedAdmin(admin.ModelAdmin):
    list_display = ['telephone','rg','cpf','cep','birthdate','address','city','state','country',]



admin.site.register(Bank,BankAdmin)
admin.site.register(Verified,VerifiedAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)




