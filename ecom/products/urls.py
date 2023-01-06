from django.urls import path
from . import views
urlpatterns = [
    path('allproduct/',views.ProductList.as_view(),name='register'),
]
