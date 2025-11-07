from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='booking')
router.register(r'menu', views.MenuViewSet, basename='menu')


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings', views.bookings, name='bookings'),

    # API routes (DRF viewsets)
    path('api/', include(router.urls)),

    # Authentication endpoints provided by djoser (token auth)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]