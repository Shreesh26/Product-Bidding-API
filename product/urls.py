from django.urls import include, path
from . import views
from django.conf import settings
#from django.conf.urld.static import static

urlpatterns = [
    path("all_product/", views.AllProduct().as_view(), name="GetAllProducts"),
    path('view_product/', views.ViewProduct().as_view(), name="view_prod"),
    path('add_product/', views.AddProduct().as_view(), name="add_product"),
    path('view_bid/', views.ViewBid().as_view(), name="view_bids"),
    path("bid/", views.PlaceBid().as_view(), name="bid"),
    path("final/", views.FinalizeBid().as_view(), name="final"),
    path('search/', views.ProductSearch().as_view(), name="search")
]