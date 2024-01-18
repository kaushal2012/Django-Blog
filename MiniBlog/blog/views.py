from django.shortcuts import render
from faker import Faker


# Create your views here.
def home(request):
    def generate_blog_text():
        fake = Faker()
        return fake.text(max_nb_chars=800)

    return render(request, 'blog/home.html', {'blog_text': generate_blog_text()})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def dashboard(request):
    return render(request, 'blog/dashboard.html')


def login(request):
    return render(request, 'blog/login.html')


def signup(request):
    return render(request, 'blog/signup.html')
