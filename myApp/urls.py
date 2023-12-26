from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('', views.home),
    # path('products/', views.products),
    # path('customer/', views.customer),
    # path('drinks/', views.drink_list),
    # path('drinks/<int:id>', views.drink_detail),
    path('advance-stats/', views.advance_stats_list),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    # path('advance-stats/<int:pk>/', views.advance_stats_detail)
    path('json-data/', views.json_data_view, name='json-data'),
    path('get-player-per/', views.get_player_per, name='get-player-per'),
    path('api/player_efficiency_ratings/<str:username>/', views.get_player_efficiency_ratings, name='get_player_efficiency_ratings'),
    # New API endpoint for the leaderboard
    path('api/leaderboard/<str:username>/', views.leaderboard, name='leaderboard'),
    path('api/leaderboard-list/', views.leaderboard_list, name='leaderboard_list'),
    path('api/get_correct_picks/', views.get_correct_picks, name='get_correct_picks_list'),  # A unique name for the list view
    path('api/get_correct_picks/<str:username>/', views.user_data, name='user_data_detail')
]


urlpatterns = format_suffix_patterns(urlpatterns)