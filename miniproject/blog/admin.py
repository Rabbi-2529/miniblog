from django.contrib import admin
from .models import upload
# Register your models here.
@admin.register(upload)
class postModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']

 
