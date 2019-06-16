from django.contrib import admin
from rango.models import Category, Page


class PageInline(admin.TabularInline):
    model = Page
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes', 'slug')
    inlines = [PageInline]


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Page Details', {'fields':['title', 'url']}), 
        ('Which Category', {'fields':['category']})
    ]
    list_display = ('title', 'category', 'url', 'views')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
