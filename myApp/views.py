from rest_framework.decorators import api_view
from rest_framework.response import Response
from basketball_reference_web_scraper import client
from .models import AdvanceStats
from .serializers import AdvanceStatsSerializer

@api_view(['GET'])
def advance_stats_list(request):
    if request.method == 'GET':
        try:
            # Use the basketball_reference_web_scraper to fetch player advanced statistics data
            player_stats = client.players_advanced_season_totals(
                season_end_year=2022
            )  # Replace with the desired season year

            # Initialize an empty list to store serialized player stats
            players_stats = []

            # Deserialize and validate each player's data
            for stats in player_stats:
                serializer = AdvanceStatsSerializer(data=stats)
                if serializer.is_valid():
                    players_stats.append(serializer.data)
                else:
                    # Handle invalid data if needed
                    pass

            # Sort the data based on the specified fields in descending order
            sorted_stats = sorted(players_stats, key=lambda x: (
                -x.get('win_shares', 0),
                -x.get('win_shares_per_48_minutes', 0),
                -x.get('box_plus_minus', 0),
                -x.get('value_over_replacement_player', 0),
            ))

            # Get the top 20 players
            top_20_players = sorted_stats[:20]

            # Save the top 20 players' data to the database
            for player_data in top_20_players:
                AdvanceStats.objects.create(
                    name=player_data['name'],
                    minutes_played=player_data['minutes_played'],
                    games_played=player_data['games_played'],
                    three_point_attempt_rate=player_data['three_point_attempt_rate'],
                    total_rebound_percentage=player_data['total_rebound_percentage'],
                    win_shares=player_data['win_shares'],
                    win_shares_per_48_minutes=player_data['win_shares_per_48_minutes'],
                    box_plus_minus=player_data['box_plus_minus'],
                    value_over_replacement_player=player_data['value_over_replacement_player']
                )

            # Return the top 20 players' data as a JSON response
            return Response(top_20_players)
        except Exception as e:
            return Response({'detail': str(e)}, status=500)
