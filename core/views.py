import requests

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from .models import CropAnalysis
from .services.ai_service import analyze_crop_image


def home(request):
    return render(request, "core/index.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistrationForm()

    return render(request, "core/auth/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("dashboard")

            form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "core/auth/login.html", {"form": form})


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/dashboard.html")


def scanner(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        image = request.FILES.get("crop_image")

        if image:
            analysis = CropAnalysis.objects.create(
                user=request.user,
                image=image
            )

            result = analyze_crop_image(analysis.image.path)

            analysis.crop_name = result["crop_name"]
            analysis.health_status = result["health_status"]
            analysis.possible_disease = result["possible_disease"]
            analysis.care_advice = result["care_advice"]
            analysis.save()

            return render(
                request,
                "core/scanner.html",
                {
                    "analysis": analysis,
                    "confidence": result["confidence"]
                }
            )

    return render(request, "core/scanner.html")


def recommendation(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/recommendation.html")


def weather(request):
    if not request.user.is_authenticated:
        return redirect("login")

    try:
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": 14.4674,
            "longitude": 78.8241,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "daily": "precipitation_probability_max",
            "timezone": "auto"
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        weather_data = {
            "temperature": data["current"]["temperature_2m"],
            "humidity": data["current"]["relative_humidity_2m"],
            "wind": data["current"]["wind_speed_10m"],
            "rain_chance": data["daily"]["precipitation_probability_max"][0],
        }


    except Exception as error:
        print("Weather API Error:", error)

        weather_data = {
            "temperature": 28,
            "humidity": 65,
            "wind": 12,
            "rain_chance": 30,
        }


    return render(
        request,
        "core/weather.html",
        {"weather": weather_data}
    )


def irrigation(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/irrigation.html")


def market(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/market.html")


def ai_assistant(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/ai_assistant.html")