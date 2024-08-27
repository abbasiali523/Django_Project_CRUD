from django.contrib import admin
from .models import Post , Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'author')
    list_filter = ('date_posted',)
    date_hierarchy = 'date_posted'


admin.site.register(Post , PostAdmin)
admin.site.register(Comment)

# Register your models here.
