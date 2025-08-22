from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import * #após montar a tabela no Models é necessário acrescentar aqui para migrar para o site


admin.site.register(Token)
admin.site.register(UserToken)
admin.site.register(Transaction)
admin.site.register(Moves)
