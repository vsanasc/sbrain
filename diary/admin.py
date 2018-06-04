from django.contrib import admin

from diary.models import (
    Date,
    Dedication,
    TypeDedication,
    Role,
    Schedule,
    TypeSchedule,
    SmallNote,
    Task,
    TypeTask
)


class SmallNoteInline(admin.TabularInline):
    model = SmallNote
    extra = 0


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0


class DedicationInline(admin.TabularInline):
    model = Dedication
    extra = 0


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('date', 'stars',)
    inlines = [SmallNoteInline, ScheduleInline, DedicationInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(DateAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(DateAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs


@admin.register(TypeTask)
class TypeTaskAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TypeTaskAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TypeTaskAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

@admin.register(TypeDedication)
class TypeDedicationAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TypeDedicationAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TypeDedicationAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoleAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(RoleAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

@admin.register(TypeSchedule)
class TypeScheduleAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TypeScheduleAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TypeScheduleAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)

        return qs

