from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    return HttpResponse("hey,<h1> welcome </h1>")


def r_n(request, name):
    return render(request, "hello/index.html", {
        'name': name.capitalize()
    })