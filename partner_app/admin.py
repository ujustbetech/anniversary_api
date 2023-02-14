from django.contrib import admin
from  . models  import partner,postimage

# Register your models here.
# admin.site.register(partner)
class postimageAdmin(admin.StackedInline):
    model = postimage
 
@admin.register(partner)
class PostAdmin(admin.ModelAdmin):
    inlines = [postimageAdmin]
 
    class Meta:
       model = partner
 
@admin.register(postimage)
class postimageAdmin(admin.ModelAdmin):
    pass