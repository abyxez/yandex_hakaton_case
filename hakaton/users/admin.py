from django.contrib.admin import ModelAdmin, register

from users.models import User


@register(User)
class UserAdmin(ModelAdmin):
    """Настройки для админ зоны пользователей"""
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'job_title',
        
    )
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)
    empty_value_display = '-empty-'
