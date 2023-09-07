from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

# Get all player box scores for January 1st, 2017 
client.player_box_scores(day=1, month=1, year=2017)

# Output all player box scores for January 1st, 2017 in JSON format to 1_1_2017_box_scores.json
client.player_box_scores(day=1, month=1, year=2022, output_type=OutputType.JSON, output_file_path="./1_1_2022_box_scores.json")
