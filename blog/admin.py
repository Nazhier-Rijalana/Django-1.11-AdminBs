from django.contrib import admin

# Register your models here.

from .models import Blog

class BlogModelAdmin(admin.ModelAdmin):
    list_display = ("__unicode__","timestamp","updated","content")
    list_display_link = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title", "content","updated"]
    class Meta:
        model = Blog

admin.site.register(Blog, BlogModelAdmin)
