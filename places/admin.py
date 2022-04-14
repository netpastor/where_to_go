from django.contrib import admin

from .models import Place, PlaceImage


class PlaceImageInlineAdmin(admin.TabularInline):
    model = PlaceImage


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (PlaceImageInlineAdmin,)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Place, PlaceAdmin)
