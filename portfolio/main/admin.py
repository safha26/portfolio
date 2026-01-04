from collections.abc import tuple_iterator

from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']

@admin.register(Skill)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category']
    list_filter = ['level', 'category']
    search_fields = ['name']

@admin.register(Experience)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'currently_working']
    list_filter = ['currently_working']
    search_fields = ['role', 'company']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'end_year']
    search_fields = ['degree', 'school']

@admin.register(Certification)

class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'issue_date']
    list_filter = ['issue_date']
    search_fields = ['title', 'issuer']

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profession', 'email']
