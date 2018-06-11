from django.contrib import admin

from core.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TagAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs
