from django.urls import path
from . import views

urlpatterns = [
    path('houses/', views.ListHouses.as_view(), name='list-houses'),
    path('houses/user/', views.ListUserHouses.as_view(), name='list-user-houses'),
    path('houses/user/create/', views.CreateUserHouse.as_view(), name='create-user-house'),
    path('houses/user/<int:pk>/delete/', views.DeleteUserHouse.as_view(), name='delete-user-house'),
    path('houses/user/<int:pk>/update/', views.UpdateUserHouse.as_view(), name='update-user-house'),
    path('houses/city/<str:city>/', views.ListCityHouses.as_view(), name='list-city-houses'),
]
