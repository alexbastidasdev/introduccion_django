from django.urls import path
from .views import BlogListView

app_name="blog"

urlPatterns = [
    path('', BlogListView.as_view(), name="home")
]