thonfrom datetime import datetime

def format_publish_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ").strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return date_str