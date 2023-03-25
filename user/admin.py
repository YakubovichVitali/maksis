from django.contrib import admin

from user.models import MaksisUser


@admin.register(MaksisUser)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ref_id',
        'ref_level',
    )
