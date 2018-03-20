from django.contrib import admin

from finance.models import Installment


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    pass
