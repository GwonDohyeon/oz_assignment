from django.contrib import admin
from blog.models import Blog,Comment
from django_summernote.admin import SummernoteModelAdmin

class CommentInline(admin.TabularInline):
    model=Comment
    fields=['content','author']
    extra=1
@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields=['content',]
    inlines=[CommentInline]
#admin.site.register(Blog,BlogAdmin)<--어노테이션 없이