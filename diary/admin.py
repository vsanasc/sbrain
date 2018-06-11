from django.contrib import admin
from django import forms
from diary.models import (
    Date,
    Dedication,
    GeneralType,
    Schedule,
    TypeSchedule,
    SmallNote,
    Task,
    TypeTask
)


class SmallNoteInline(admin.TabularInline):
    exclude = ('status',)
    model = SmallNote
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = GeneralType.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                SmallNoteInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


class ScheduleInline(admin.TabularInline):
    exclude = ('status',)
    model = Schedule
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = TypeSchedule.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                ScheduleInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


class DedicationInline(admin.TabularInline):
    exclude = ('status',)
    model = Dedication
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = GeneralType.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                DedicationInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


class TaskInline(admin.TabularInline):
    exclude = ('status',)
    model = Task
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if (
            db_field.name == 'type'
        ):

            try:
                kwargs['queryset'] = TypeTask.objects.filter(
                                                    user=request.user,
                                                    status=1
                                                )
            except IndexError:
                pass

        return super(
                TaskInline,
                self
            ).formfield_for_foreignkey(
                db_field,
                request,
                **kwargs
            )


@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('date', 'stars',)
    inlines = [
                SmallNoteInline,
                TaskInline,
                ScheduleInline,
                DedicationInline,
            ]

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


@admin.register(GeneralType)
class GeneralTypeAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(GeneralTypeAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(GeneralTypeAdmin, self).get_queryset(request)
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
