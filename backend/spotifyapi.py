import requests
import json

token = "BQDcjfV_iAV3qLEEkeX5po1qXBz1MtXLuFhLrvC8ibzXyWvWtNYWYOdO0NP2LiKAFDsH7X6--oatIA5rMMqdjGQtNhc3xY2qsHrHQhdI9vdqzFUk_-8"

dbr = "54Y471E7GNBSOXjZtqONId"
rodeo = "4PWBTB6NYSKQwfo79I3prg"
birds = "42WVQWuf1teDysXiOupIZt"
huncho = "6FED8aeieEnUWwQqAO9zT1"
astro = "41GuZcammIkupMPKH2OJ6I"
jackboys = "1Sf8GsXG32t0jNrX11xqWx"
utopia = "18NOKLkZETa4sWwLMIm0UZ"

headers = {
    "Authorization": f"Bearer  {token}"
}

params = {
    "ids": f"{dbr},{rodeo},{birds},{huncho},{astro},{jackboys},{utopia}"
}

album_info = requests.get(f"https://api.spotify.com/v1/albums", headers=headers, params=params)
with open("songdata.json", "w") as file:
    albums_json = album_info.json()
    for album in albums_json["albums"]:
        del album["available_markets"]
        del album["external_urls"]
        del album["href"]
        del album["release_date_precision"]
        del album["artists"]
        for song in album["tracks"]["items"]:
            del song["available_markets"]
            del song["href"]
            del song["uri"]
    file.write(json.dumps(albums_json))

