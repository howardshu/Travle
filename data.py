from song import Song

DBR = 0
RODEO = 1
BIRDS = 2
HUNCHO = 3
ASTRO = 4
JACKBOYS = 5
UTOPIA = 6

albums = ["Days Before Rodeo", "Rodeo", "Birds In The Trap Sing McKnight", "Huncho Jack, Jack Huncho"
          "Astroworld", "Jackboys", "Utopia"]

# 12 + 16 + 14 + 13 + 17 + 7 + 19 = 98 songs in catalog
songs = []

def get_songs():
    # TODO: Spotify API stuff
    # ORDER FEATURE NAMES ALPHABETICALLY
    songs.append(Song("FE!N", 8, UTOPIA, "3:11", ["Playboi Carti", "Sheck Wes"]))
    songs.append(Song("Flying High", 12, RODEO, "3:28", ["Toro y Moi"]))
    songs.append(Song("STARGAZING", 1, ASTRO, "4:30", []))