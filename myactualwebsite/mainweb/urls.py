from django.urls import path
from . import views

app_name = "mainweb"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('thankyou/', views.thankyou, name="thankyoupage")
]