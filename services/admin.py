from django.contrib import admin
from .models import *


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContactRequest, ContactAdmin)