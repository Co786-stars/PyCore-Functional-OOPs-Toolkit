from django.contrib import admin
from django.urls import path
from . import views   # import views from the same app

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Static routes
    path('securepage/', views.securepage, name='securepage'),
    path('xyz/', views.new_admin, name='new_admin'),

    # Dynamic routes
    path('xyz/<int:dynamic_route>/', views.new_admin_details, name="routing1"),
    # captures integer values like /xyz/15/

    path('dynamic_route/<str:wizard>/', views.d2fill_in_depth, name="routing2"),
    # captures string values like /dynamic_route/aditya/

    path('fill/<int:id>/', views.d3nothing_fill, name="routing3"),
    # captures integer values like /fill/99/

    # Basic practice
    path('pqr/', views.new_fun, name="newz_fun_practice"),

    # Homepage route (render index.html)
    path('', views.homepage, name="homepage"),
]


