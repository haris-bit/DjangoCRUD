from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    # path('', views.home),
    # path('products/', views.products),
    # path('customer/', views.customer),
    # path('drinks/', views.drink_list),
    # path('drinks/<int:id>', views.drink_detail),
    path('advance-stats/', views.advance_stats_list),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    # path('advance-stats/<int:pk>/', views.advance_stats_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)