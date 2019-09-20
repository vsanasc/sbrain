from django.contrib import admin

from finance.models import (
    ExpenseCategory,
    ExpenseType
)


class ExpenseTypeInlineAdmin(admin.TabularInline):
    model = ExpenseType
    min_num = 1
    extra = 1


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'created_at',)
    list_editable = ('order',)
    inlines = (ExpenseTypeInlineAdmin,)
