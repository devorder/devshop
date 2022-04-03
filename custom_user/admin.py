from django.contrib import admin
from .models import UserAccountCustomModel
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'is_active')
    list_display_links = ('email', 'username')
    read_only_fileds = ('last_login',)
    ordering = ('-last_login',)

    filter_horizontal = ()
    list_filter = ()
    # set password to not showupin admin form.
    fieldsets = ()


# Register your models here.
admin.site.register(UserAccountCustomModel, CustomUserAdmin)