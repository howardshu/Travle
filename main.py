# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from data import songs
import random
import re

if __name__ == '__main__':
    target = random.choice(songs)
    songTitle = input("Enter a song title: ")
    songHit = None
    search = []
    for song in songs:
        if song.title == songTitle:
            songHit = song
            break
        elif re.search(songTitle, song.title, re.IGNORECASE):
            search.append(song)

    if songHit is not None:
        target.check_match(songHit)
    else:
        print(search)

