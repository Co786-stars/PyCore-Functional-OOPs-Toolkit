from django.http import HttpResponse

# static routes
def securepage(request):
    return HttpResponse("This page belongs to cryptoCore")

def new_admin(request):
    return HttpResponse("<h2>This.................cryptoCore</h2>")

# dynamic routes
def new_admin_details(request, dynamic_route):
    # dynamic_route will be an integer from the URL
    return HttpResponse(f"This is routing 1st, value = {dynamic_route}")

def d2fill_in_depth(request, wizard):
    # wizard will be a string from the URL
    return HttpResponse(f"This is routing 2nd, value = {wizard}")

def d3nothing_fill(request, id):
    # id will be an integer from the URL
    return HttpResponse(f"{id} This is routing 3rd")

