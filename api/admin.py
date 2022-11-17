from django.contrib import admin
from . import models

admin.site.register(models.Sponsor)
admin.site.register(models.Student)
admin.site.register(models.OTM)
admin.site.register(models.SponsorPayForStudent)

# @admin.register(models.Sponsor)
# class SponsorAdmin(admin.ModelAdmin):
#     list_display = ("id", "fish", "")