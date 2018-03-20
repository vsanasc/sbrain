
from django.contrib import admin

from finance.models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name', 'value', 'date',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
