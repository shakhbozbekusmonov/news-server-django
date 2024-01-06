from django.contrib import admin

from news.models import News, Category


admin.site.register(Category)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    prepopulated_fields = {"slug": ('title', )}


admin.site.site_header = 'News Admin'
admin.site.site_title = 'News site admin'