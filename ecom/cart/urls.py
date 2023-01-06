from django.urls import path
from . import views
urlpatterns = [
  path('addcart/<int:id>',views.Addcart,name="addcart")
]
