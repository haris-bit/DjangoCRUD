from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('', views.home),
    # path('products/', views.products),
    # path('customer/', views.customer),
    # path('drinks/', views.drink_list),
    # path('drinks/<int:id>', views.drink_detail),
    path('advance-stats/', views.advance_stats_list),
    # path('advance-stats/<int:pk>/', views.advance_stats_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)