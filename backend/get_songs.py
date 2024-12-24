from song import Song
import csv

# 12 + 16 + 14 + 13 + 17 + 7 + 19 = 98 songs in catalog
songs = []

def get_songs():
    with open("songdata.csv", "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            songs.append(Song(row[0], int(row[1]), int(row[2]), row[3], row[4:]))
            # print(f"{row[0]}, {int(row[1])}, {int(row[2])}, {row[3]}, {row[4:]}")