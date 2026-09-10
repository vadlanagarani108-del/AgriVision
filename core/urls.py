from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("scanner/", views.scanner, name="scanner"),
    path("recommendation/", views.recommendation, name="recommendation"),

    path("weather/", views.weather, name="weather"),
    path("irrigation/", views.irrigation, name="irrigation"),
    path("market/", views.market, name="market"),
    path("ai-assistant/", views.ai_assistant, name="ai_assistant"),
]