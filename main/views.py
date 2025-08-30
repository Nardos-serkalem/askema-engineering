from django.shortcuts import render
from .models import News, Award, Testimonial

def home(request):
    news = News.objects.all().order_by('-published_date')[:3]
    awards = Award.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "home.html", {"news": news, "awards": awards, "testimonials": testimonials})

def about(request):
    return render(request, "about.html")

def awards(request):
    awards = Award.objects.all()
    return render(request, "awards.html", {"awards": awards})

def news(request):
    news = News.objects.all()
    return render(request, "news.html", {"news": news})

def contact(request):
    return render(request, "contact.html")

def login_view(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

