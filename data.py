DBR = 0
RODEO = 1
BIRDS = 2
HUNCHO = 3
ASTRO = 4
JACKBOYS = 5
UTOPIA = 6

albums = ["Days Before Rodeo", "Rodeo", "Birds In The Trap Sing McKnight", "Huncho Jack, Jack Huncho",
          "Astroworld", "Jackboys", "Utopia"]

from song import Song

# 12 + 16 + 14 + 13 + 17 + 7 + 19 = 98 songs in catalog
songs = []

def get_songs():
    # TODO: Spotify API stuff
    # ORDER FEATURE NAMES ALPHABETICALLY
    songs.append(Song("FE!N", UTOPIA, 8, "3:11", ["Playboi Carti", "Sheck Wes"]))
    songs.append(Song("Flying High", RODEO, 12, "3:28", ["Toro y Moi"]))
    songs.append(Song("STARGAZING", ASTRO, 1, "4:30", []))