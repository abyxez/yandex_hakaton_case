from django.contrib.admin import ModelAdmin, register

from users.models import User


@register(User)
class UserAdmin(ModelAdmin):
    """Настройки для админ зоны пользователей"""
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'job_title',
        
    )
    search_fields = ('email','username')
    list_filter = ('email','username')
    empty_value_display = '-empty-'
