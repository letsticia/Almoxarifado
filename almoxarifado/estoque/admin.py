from django.contrib import admin
from estoque.models import LogSaida, LogEntrada

# Register your models here.
admin.site.register(LogSaida)
admin.site.register(LogEntrada)