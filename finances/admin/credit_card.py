
from django.contrib import admin

from finances.models import CreditCard, CreditCardBill

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
	exclude = ('user',)
	list_display = ('name','type','limit',)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(CreditCardAdmin, self).get_queryset(request)
		if not request.user.is_superuser:
			return qs.filter(user=request.user)

		return qs


@admin.register(CreditCardBill)
class CreditCardBillAdmin(admin.ModelAdmin):
	exclude = ('user',)
	list_display = ('credit_card','total',)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(CreditCardBillAdmin, self).get_queryset(request)
		if not request.user.is_superuser:
			return qs.filter(user=request.user)

		return qs