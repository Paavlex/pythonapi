from django.urls import path
from . import views


#URLs pro API a svazani s views
urlpatterns = [
    path('', views.vulnerabiltyOverview, name="vulnerabilityOverview"),
    path('vulnerability-save/', views.vulnerablitySave, name="vulnerability-save"),
    path('vulnerability-list/', views.vulnerabilityList, name="vulnerability-list"),
    path('vulnerability-search/<str:whatToSearch>/', views.vulnerabilitySearch, name="vulnerability-search"),
]