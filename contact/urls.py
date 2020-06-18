from django.urls import path
from contact import views
urlpatterns = [
    path('', views.send_email, name="email"),
    path('success/', views.send_success, name="success"),
]