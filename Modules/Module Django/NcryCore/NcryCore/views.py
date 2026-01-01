# Import necessary Django modules
from django.http import HttpResponse       # Used to return plain text or HTML directly
from django.shortcuts import render        # Used to render HTML templates

# -------------------------------
# STATIC ROUTES (fixed URLs)
# -------------------------------

def securepage(request):
    """
    A simple static route.
    When user visits /securepage/, this function runs.
    """
    return HttpResponse("This page belongs to cryptoCore")


def new_admin(request):
    """
    Another static route.
    When user visits /xyz/, this function runs.
    """
    return HttpResponse("<h2>This.................cryptoCore</h2>")


# -------------------------------
# DYNAMIC ROUTES (URLs with variables)
# -------------------------------

def new_admin_details(request, dynamic_route):
    """
    Example of capturing an integer from the URL.
    URL: /xyz/15/ → dynamic_route = 15
    """
    return HttpResponse(f"This is routing 1st, value = {dynamic_route}")


def d2fill_in_depth(request, wizard):
    """
    Example of capturing a string from the URL.
    URL: /dynamic_route/aditya/ → wizard = "aditya"
    """
    return HttpResponse(f"This is routing 2nd, value = {wizard}")


def d3nothing_fill(request, id):
    """
    Example of capturing another integer from the URL.
    URL: /fill/99/ → id = 99
    """
    return HttpResponse(f"{id} This is routing 3rd")


# -------------------------------
# BASIC PRACTICE FUNCTION
# -------------------------------

def new_fun(request):
    """
    Just a simple loop example.
    It runs a loop from 1 to 2, and finally returns 2.
    URL: /pqr/
    """
    for i in range(1, 3):
        x = i
    return HttpResponse(x)   # Output will be 2


# -------------------------------
# HOMEPAGE (Rendering HTML template)
# -------------------------------

def homepage(request):
    """
    Example of rendering an HTML template.
    It looks for 'index.html' inside your templates folder.
    URL: /
    """
    return render(request, "index.html")   # render(request, template_name)
