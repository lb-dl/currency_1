from account.models import Avatar, User

from django.contrib import admin


class AvatarInline(admin.TabularInline):
    # class AvatarInline(admin.StackedInline):

    model = Avatar
    extra = 0


class UserAdmin(admin.ModelAdmin):
    inlines = (AvatarInline, )
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
    ]
    list_filter = [
        'date_joined',
        'groups'
    ]
    readonly_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )
    search_fields = (
        'first_name',
        'last_name'
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.has_perm('account.full_edit') \
                or request.user.is_superuser:
            return ()
        return super().get_readonly_fields(request, obj=obj)


class AvatarAdmin(admin.ModelAdmin):
    readonly_fields = ('user', )
    # raw_id_fields = ['user', ]
    list_display = ('id', 'user')
    list_select_related = ['user']  # Avatar.objects.select_related('user')


admin.site.register(User, UserAdmin)
admin.site.register(Avatar, AvatarAdmin)
