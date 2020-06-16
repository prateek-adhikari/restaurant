from django.urls import path
from blog import views
urlpatterns = [
    path('', views.post_list, name="postlist"),
    path('<int:pk>', views.post_detail, name="postdetail"),
]