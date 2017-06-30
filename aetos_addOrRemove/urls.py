from django.conf.urls import url
from aetos_addOrRemove import views


urlpatterns = [
    url(r'^create/', views.CreateFoodTruck.as_view(), name='create-food-truck'),
    url(r'^remove/', views.RemoveFoodTruck.as_view(), name='delete-food-truck')
]