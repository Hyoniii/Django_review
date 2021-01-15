#from django.contrib import admin
#from user.models    import User
#
from django.contrib            import admin
from django.contrib.auth       import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    list_display = ('email','username','phone_number','address','gender',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {
            'fields': ( 'gender', 'address'),
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {
            'fields': ( 'gender', 'address'),
        }),
    )


admin.site.register(User, UserAdmin)
#admin.site.register(User)
