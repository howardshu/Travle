from data import albums
import json
import csv

albums_dict = {
    "DAYS BEFORE RODEO": 0,
    "Rodeo": 1,
    "Birds In The Trap Sing McKnight": 2,
    "Huncho Jack, Jack Huncho": 3,
    "ASTROWORLD": 4,
    "JACKBOYS": 5,
    "UTOPIA": 6
}


file = open("songdata.json", "r")
albums_json = json.load(file)
songdata_csv = open("songdata.csv", "w")
csv_writer = csv.writer(songdata_csv, delimiter=';')
for album in albums_json["albums"]:
    if album["name"] not in albums:
        continue
    album_name = album["name"]
    for track in album["tracks"]["items"]:
        features = [artist["name"] for artist in track["artists"]]
        try:
            features.remove("Travis Scott")
        except ValueError:
            pass
        try:
            features.remove("JACKBOYS")
        except ValueError:
            pass
        try:
            features.remove("Huncho Jack")
        except ValueError:
            pass
        features.sort()  # order feature names alphabetically
        total_seconds = track["duration_ms"] / 1000
        minutes_str = str(int(total_seconds / 60))
        seconds = int(total_seconds % 60)
        seconds_str = "0" + str(seconds) if seconds < 10 else str(seconds)
        length = minutes_str + ":" + seconds_str
        track_number = track["track_number"]
        track_name = track["name"]
        idx = track_name.find(" (feat.")
        if idx != -1:
            track_name = track_name[:idx]
        csv_writer.writerow([track_name, albums_dict[album_name], track_number, length] + features)
