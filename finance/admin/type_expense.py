from django.contrib import admin

from finance.models import (
        CategoryTypeExpense,
        TypeExpense
    )


class TypeExpenseInlineAdmin(admin.TabularInline):
    model = TypeExpense
    min_num = 1
    extra = 1


@admin.register(CategoryTypeExpense)
class CategoryTypeExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    inlines = (TypeExpenseInlineAdmin,)
