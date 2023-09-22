from rest_framework.decorators import api_view
from rest_framework.response import Response
from basketball_reference_web_scraper import client
from .serializers import AdvanceStatsSerializer  # Import your serializer

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

            return Response(top_20_players)
        except Exception as e:
            return Response({'detail': str(e)}, status=500)
