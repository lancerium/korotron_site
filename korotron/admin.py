from django.contrib import admin


from .models import AboutUS, CategoryService, Services, Action


class AboutUSAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)


class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'price', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'category__title')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)


class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'description', 'is_published')
    list_display_links = ('id', 'photo',)
    search_fields = ('description',)
    list_editable = ('is_published',)


admin.site.register(AboutUS, AboutUSAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(Action, ActionAdmin)


