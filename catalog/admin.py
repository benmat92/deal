from django.contrib import admin

# Register your models here.
from .models import Category, Deal, Profile, Comment

#admin.site.register(Category)
#admin.site.register(Deal)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class DealAdmin(admin.ModelAdmin):
    list_filter = ('status', 'date_posted')
    prepopulated_fields = {'slug': ('title',), }
admin.site.register(Deal, DealAdmin)


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
