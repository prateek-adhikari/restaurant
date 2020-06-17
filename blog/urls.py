from django.urls import path
from blog import views
urlpatterns = [
    path('', views.post_list, name="postlist"),
    path('<int:pk>', views.post_detail, name="postdetail"),
    path('tag/<slug:tag>', views.post_by_tag, name="postbytag"),
    path('category/<slug:category>', views.post_by_category, name="postbycategory"),
]