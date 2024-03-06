from django.contrib import admin

from users.models import User
from users.models import Partner

admin.site.register(User)
admin.site.register(Partner)
