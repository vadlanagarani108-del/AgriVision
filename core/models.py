from django.db import models
from django.contrib.auth.models import User


class FarmerProfile(models.Model):
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("te", "Telugu"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=150, blank=True)
    preferred_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default="en"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class CropAnalysis(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to="crop_scans/")
    crop_name = models.CharField(max_length=100, blank=True)
    health_status = models.CharField(max_length=100, blank=True)
    possible_disease = models.CharField(max_length=200, blank=True)
    care_advice = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop_name or 'Crop Scan'} - {self.created_at:%Y-%m-%d}"


class FarmRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=150, blank=True)
    planting_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name