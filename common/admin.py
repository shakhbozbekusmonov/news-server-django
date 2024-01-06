from django.contrib import admin

from news.models import News, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryAdmin)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_at', 'status']
    list_filter = ['status', 'created_at', 'published_at']
    prepopulated_fields = {"slug": ('title', )}
    date_hierarchy = 'published_at'
    search_fields = ['title', 'body']
    ordering = ['status', 'published_at']


admin.site.site_header = 'News Admin'
admin.site.site_title = 'News site admin'