from django.contrib.admin import ModelAdmin, register

from users.models import User
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin


@register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','first_name','last_name','job_title',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','job_title',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','first_name','last_name','job_title',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)