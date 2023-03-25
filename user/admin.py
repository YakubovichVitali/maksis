from django.contrib import admin

from user.models import MaksisUser


@admin.register(MaksisUser)
class MaksisUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ref_id',
        'ref_level',
    )
