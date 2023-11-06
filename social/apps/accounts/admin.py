from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_login', 'is_superuser', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'photo')
    list_display_links = ('email', 'photo')
    search_fields = ('email', 'first_name')


admin.site.register(UserAccount, UserAccountAdmin)
