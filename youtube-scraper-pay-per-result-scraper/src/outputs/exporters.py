thonimport csv

def export_to_csv(videos, filename="output.csv"):
    keys = videos[0].keys() if videos else []
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(videos)