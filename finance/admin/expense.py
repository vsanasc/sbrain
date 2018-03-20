
from django.contrib import admin
from finance.models import Expense
from finance.models import TypeExpense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('type', 'value', 'method', 'date',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'type':
            # import pdb; pdb.set_trace()
            kwargs['queryset'] = TypeExpense.objects.filter(user=request.user)

        return super(ExpenseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(ExpenseAdmin, self).get_queryset(request)

        if not request.user.is_superuser:
            return qs.filter(user=request.user).order_by('-date')

        return qs

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ExpenseAdmin, self).save_model(request, obj, form, change)
