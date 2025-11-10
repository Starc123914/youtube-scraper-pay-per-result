thondef parse_video_data(data):
    videos = []
    for item in data.get('items', []):
        video = {
            "type": item.get('id', {}).get('kind', ''),
            "id": item.get('id', {}).get('videoId', ''),
            "title": item.get('snippet', {}).get('title', ''),
            "url": f"https://www.youtube.com/watch?v={item.get('id', {}).get('videoId', '')}",
            "description": item.get('snippet', {}).get('description', ''),
            "views": 0,  # Placeholder, as this data isn't available from search results
            "likes": 0,  # Placeholder, as this data isn't available from search results
            "channel": {
                "id": item.get('snippet', {}).get('channelId', ''),
                "name": item.get('snippet', {}).get('channelTitle', ''),
                "url": f"https://www.youtube.com/channel/{item.get('snippet', {}).get('channelId', '')}"
            },
            "publishDate": item.get('snippet', {}).get('publishedAt', ''),
            "duration": 0,  # Placeholder
            "thumbnails": item.get('snippet', {}).get('thumbnails', {}).get('high', {}).get('url', '')
        }
        videos.append(video)
    return videos