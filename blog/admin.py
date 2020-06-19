from django.contrib import admin
from blog.models import Post,Category,Comment
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Post, PostAdmin)

admin.site.register([
    Category,
    Comment,
])