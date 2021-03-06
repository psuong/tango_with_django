from django.contrib import admin
# Import the necessary modules from models
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Page)
admin.site.register(Page, PageAdmin)
