from django.contrib import admin

from .models import (
    User,
    SocialApp,
    SocialUser,
)

admin.site.register(User)
admin.site.register(SocialApp)
admin.site.register(SocialUser)
