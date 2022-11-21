from django.contrib import admin
from . import models


@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("id", "fish", "phone_number", "payment", "spent_amount", "status", "created_at",)
    list_display_links = ("id", "fish")
    list_filter = ("status", "payment", "created_at", "updated_at")
    search_fields = ("fish",)
    readonly_fields = ("spent_amount",)
    fieldsets = (("Main", {"fields": ("fish", "phone_number", "payment", "spent_amount", "status")}),)


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "fish", "student_type", "otm", "allocated_amount", "contract_amount",)
    list_display_links = ("id", "fish")
    list_filter = ("student_type", "otm__name")
    search_fields = ("fish",)
    readonly_fields = ("allocated_amount",)
    fieldsets = (("Main", {"fields": ("fish", "phone_number", "otm", "allocated_amount", "student_type", "contract_amount")}),)


@admin.register(models.OTM)
class OTMAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_display_links = ("id", "name")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    fieldsets = (("Main", {"fields": ("name",)}),)


@admin.register(models.SponsorPayForStudent)
class SponsorPayForStudentAdmin(admin.ModelAdmin):
    list_display = ("id", "sponsor", "student", "amount", "created_at")
    list_display_links = ("id", "sponsor", "student")
    list_filter = ("created_at", "updated_at")
    search_fields = ("sponsor",)
    fieldsets = (("Main", {"fields": ("sponsor", "student", "amount")}),)
