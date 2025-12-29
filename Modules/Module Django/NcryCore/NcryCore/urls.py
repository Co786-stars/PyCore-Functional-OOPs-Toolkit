"""
URL configuration for NcryCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
]
