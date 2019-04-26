from django.contrib import admin

from finance.models import (
    IncomeType
)


@admin.register(IncomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'currency', 'created_at',)
    exclude = ('user',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'type':
            kwargs['queryset'] = IncomeType.objects.filter(user=request.user)

        return super(
                    IncomeTypeAdmin,
                    self
                ).formfield_for_foreignkey(
                    db_field,
                    request,
                    **kwargs
                )

    def get_queryset(self, request):
        qs = super(IncomeTypeAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            return qs.filter(user=request.user).order_by('-date')

        return qs

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(IncomeTypeAdmin, self).save_model(request, obj, form, change)
