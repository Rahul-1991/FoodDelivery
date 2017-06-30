from django.conf.urls import url
from aetos_search import views


urlpatterns = [
    url(r'^name/', views.NameSearch.as_view(), name='name-search'),
    url(r'^street/', views.StreetSearch.as_view(), name='street-search')
]
