from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug:slug>/', views.category_page, name='category'),

    # Post CRUD
    path('post_<int:post_id>/', views.post_page, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('post_<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post_<int:post_id>/delete/', views.delete_post, name='delete_post'),

    # User profile with posts
    path('user/<str:username>/', views.profile, name='profile'),

    # Add comment to post
    path('post_<int:post_id>/comment', views.add_comment, name='comment'),

    # Following feature
    path('user/<str:username>/follow', views.follow, name='follow'),
    path('user/<str:username>/unfollow', views.unfollow, name='unfollow'),
]

