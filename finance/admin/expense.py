
from django.contrib import admin
from finance.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	exclude = ('user',)
	list_display = ('type','value','method','date',)

	def get_queryset(self, request):
		qs = super().get_queryset(request)

		if not request.user.is_superuser:
			return qs.filter(user=request.user).order_by('-date')

		return qs

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)
