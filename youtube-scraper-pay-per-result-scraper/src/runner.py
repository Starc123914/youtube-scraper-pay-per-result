thonimport json
import requests
from extractors.youtube_parser import parse_video_data
from outputs.exporters import export_to_csv
from config.settings import CONFIG

def run_scraper(query):
    # Fetch YouTube data based on the query
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={CONFIG['YOUTUBE_API_KEY']}"
    response = requests.get(url)
    data = response.json()
    
    # Parse the data
    videos = parse_video_data(data)
    
    # Export the results
    export_to_csv(videos)

if __name__ == "__main__":
    query = "Python programming tutorial"
    run_scraper(query)