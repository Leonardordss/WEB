from django.contrib import admin

# Register your models here.
from .models import * #após montar a tabela no Models é necessário acrescentar aqui para migrar para o site

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Plan)
admin.site.register(UserPlan)
admin.site.register(FavoriteMovie)
