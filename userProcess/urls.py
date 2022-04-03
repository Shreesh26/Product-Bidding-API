from django.urls import include, path
from . import views

urlpatterns = [
    path('sign_up/', views.SignUp().as_view(), name='sign_up'),
]