from data import albums
import string


class Song:
    def __init__(self, title, number, album, length, features):
        self.title = title
        self.album = album  # int based on constants from data.py
        self.number = number
        self.length = length
        self.features = features # array of strings
        # self.streams = streams # load from Spotify API

    def check_match(self, other_song):
        print(other_song.title)
        if self.title == other_song.title:
            print("G")
        else:
            print("B")

        print(albums[other_song.album])
        numerical_comp(self.album, other_song.album, 2)

        print(other_song.number)
        numerical_comp(self.number, other_song.number, 2)

        print(other_song.length)
        otherStr = other_song.length.split(":")
        selfStr = self.length.split(':')
        otherLen = int(otherStr[0]) * 60 + int(otherStr[1])
        selfLen = int(selfStr[0]) * 60 + int(selfStr[1])
        numerical_comp(selfLen, otherLen, 30)

        print(other_song.features)
        if self.features == other_song.features:
            print("G")
        elif any(item in self.features for item in other_song.features):
            print("Y")
        else:
            print("B")


def numerical_comp(num1, num2, leeway):
    diff = num1 - num2
    if diff == 0:
        print("G")
    elif 0 < diff <= leeway:
        print("Y, U")
    elif diff >= -leeway:
        print("Y, D")
    else:
        print("B")



