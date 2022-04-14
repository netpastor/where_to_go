from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


class PlaceImageInlineAdmin(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('preview',)

    def preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width='auto',
                height='200px',
            )
        )


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (PlaceImageInlineAdmin,)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Place, PlaceAdmin)
