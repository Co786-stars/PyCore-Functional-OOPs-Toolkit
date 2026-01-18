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


    # ________________________________________________________________________________________________

    # Homepage route (render, index.html)
    # path('', views.homepage, name="homepage"), # using the ('') to directly open/target the homepage

    # Pass the data from views to templet to practice for loop
    # path('', views.main_page, name="second_page"),

    # pass the data from views to templet to practice conditional loop
    path('', views.next_page, name="other_page"),

    # ________________________________________________________________________________________________

    #simple another example Dynamic route int, if we want string then use str, slug...etc
    # path('pqr/<int:unknown>', views.inside_admin, name="simple example" )
    path('pqr/<unknown>', views.inside_admin, name="simple example" )  # if we want any random value

]


