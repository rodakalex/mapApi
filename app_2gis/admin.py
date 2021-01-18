from django.contrib import admin
from .models import *


@admin.register(Path)
class PointerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Coord)
class CoordAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeCoord)
class TypeCoordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.register(Coord, CoordAdmin)
admin.register(Path, PointerAdmin)
admin.register(TypeCoord, TypeCoordAdmin)
