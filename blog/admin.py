from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_filter = ('author', 'date', 'post_tags',)
  list_display = ('title', 'date', 'author', 'content',)


class AuthorAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email_address',)

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
