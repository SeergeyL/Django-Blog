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

    # User profile
    path('user/<str:username>/', views.profile, name='profile'),
    path('user/<str:username>/following-posts', views.profile_following_posts, name='profile_following_posts'),
    path('user/<str:username>/profile-history', views.profile_history, name='profile_history'),

    # Add comment to post
    path('post_<int:post_id>/comment', views.add_comment, name='comment'),
    path('post_<int:post_id>/comment_<int:comment_id>/delete', views.delete_comment, name='delete_comment'),

    # Following feature
    path('user/<str:username>/follow', views.follow, name='follow'),
    path('user/<str:username>/unfollow', views.unfollow, name='unfollow'),
]

