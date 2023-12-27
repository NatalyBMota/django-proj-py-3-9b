from django.urls import path
#from django.urls import include
from .views import HomePageView, CreatePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post', CreatePostView.as_view(), name='add_post'),
    #path('', include('recipes.urls')),
]