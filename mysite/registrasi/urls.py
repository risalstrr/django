from django.urls import path
# from . import views

# app_name = "main"   

# urlpatterns = [
#     path("", views.homepage, name="homepage"),
#     path("register", views.register_request, name="register")
# ]
from registrasi.views import register 
 
urlpatterns = [ 
    path('register/', register, name="register"),
] 
