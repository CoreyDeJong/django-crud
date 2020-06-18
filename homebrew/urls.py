from django.urls import path
from .views import HomeView, BeerListView, BeerDetailView, BeerCreateView, BeerUpdateView, BeerDeleteView

urlpatterns = [
    # path('', HomeView.as_view(),name="base"),
    path('', BeerListView.as_view(), name='beer_list'),
    path('beer/<int:pk>/', BeerDetailView.as_view(), name='beer_detail'),
    path('beer/new/', BeerCreateView.as_view(), name='beer_create'),
    path('beer/<int:pk>/edit/', BeerUpdateView.as_view(), name='beer_update'),
    path('beer/<int:pk>/delete/', BeerDeleteView.as_view(), name='beer_delete'),
]