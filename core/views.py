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

            form.add_error(
                None,
                "Invalid username or password."
            )
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
                    "confidence": 0
                }
            )
def recommendation(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/recommendation.html")