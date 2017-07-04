from django.conf.urls import url
from aetos_misc import views


urlpatterns = [
    url(r'^assignTruck/', views.AssignTruckView.as_view(), name='assign-truck')
]
