from django.urls import include, path
from . import views

urlpatterns = [
    path('sign_up/', views.SignUp().as_view(), name='sign_up'),
    path('edit_usr_detail/', views.UserProfile().as_view(), name="self_profile_edit"),
    path("usr_profile/", views.ViewUser().as_view(), name="view_usr_profile"),
]