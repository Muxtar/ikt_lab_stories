from django.contrib import admin
from home.models import Contact, Category, Stories, Tag

# Register your models here.


admin.site.register([Contact, Category, Tag])

@admin.register(Stories)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')
    search_fields = ('user__username', 'user__id', 'title')
    list_filter = ('title','date')
