from django.contrib import admin
from .models import *


@admin.register(Path)
class PointerAdmin(admin.ModelAdmin):
    pass


admin.register(Path, PointerAdmin)
