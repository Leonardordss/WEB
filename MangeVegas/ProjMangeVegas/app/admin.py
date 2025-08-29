from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


admin.site.register(Token)
admin.site.register(Account)
admin.site.register(AccountToken)
admin.site.register(Transaction)
admin.site.register(Bet)