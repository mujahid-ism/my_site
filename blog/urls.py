from django.urls import path
from . import views

urlpatterns = [
	path('', views.starting_page, name='starting-page'),
	path('posts', views.posts, name='post-page'),
	path('posts/<slug:slug>', views.individual_post, name='individual-post') #/posts/<slug>
]
