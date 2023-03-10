from django.contrib import admin

from .models import Approval, Project

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ("title","project", "status", "amount")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass