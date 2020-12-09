
def user_avatar_context(request):

    avatar_url = ''
    if request.user.is_authenticated:
        avatar = request.user.avatar_set.filter(is_active=True).last()
        if avatar:
            avatar_url = avatar.file_path.url

    return {'avatar': avatar_url}
