from django.contrib import admin
from .models import FarmerProfile, CropAnalysis, FarmRecord


@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "location", "preferred_language", "created_at")
    search_fields = ("user__username", "location")


@admin.register(CropAnalysis)
class CropAnalysisAdmin(admin.ModelAdmin):
    list_display = ("user", "crop_name", "health_status", "possible_disease", "created_at")
    search_fields = ("crop_name", "possible_disease")


@admin.register(FarmRecord)
class FarmRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "crop_name", "soil_type", "location", "planting_date")
    search_fields = ("crop_name", "location")