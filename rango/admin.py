from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)
# Register your models here.
