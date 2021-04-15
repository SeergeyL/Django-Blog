from django.urls import path
from users import views


urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/', views.signup, name='signup'),
]
