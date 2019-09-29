from django.urls import path
from django.views.generic.base import RedirectView
from .views import PostDetail, PostList, AboutPageView, ContactPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]