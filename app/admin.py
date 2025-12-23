from django.contrib import admin
from .models import Category,Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','category','status','author','is_featured')
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)
    
    def get_status(self, obj):
        return obj.get_status_display()

    get_status.short_description = 'Status'

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)