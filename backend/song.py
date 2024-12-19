import data
import string


class Song:
    def __init__(self, title, album, number, length, features):
        self.title = title
        self.album = album  # int based on constants from data.py
        self.number = number
        self.length = length
        self.features = features # array of strings
        # self.streams = streams # load from Spotify API

    def check_match(self, other_song):
        correct = True
        stat_string = ""
        # print(other_song.title)
        if self.title == other_song.title:
            # print("G")
            stat_string += data.GREEN
        else:
            # print("B")
            stat_string += data.BLACK
            correct = False

        # print(data.albums[other_song.album])
        stat_string += numerical_comp(self.album, other_song.album, 2)

        # print(other_song.number)
        stat_string += numerical_comp(self.number, other_song.number, 2)

        # print(other_song.length)
        other_str = other_song.length.split(":")
        self_str = self.length.split(':')
        other_len = int(other_str[0]) * 60 + int(other_str[1])
        self_len = int(self_str[0]) * 60 + int(self_str[1])
        stat_string += numerical_comp(self_len, other_len, 30)

        # print(other_song.features)
        if self.features == other_song.features:
            # print("G")
            stat_string += data.GREEN
        elif any(item in self.features for item in other_song.features):
            # print("Y")
            stat_string += data.YELLOW
        else:
            # print("B")
            stat_string += data.BLACK

        return correct, stat_string


def numerical_comp(num1, num2, leeway):
    ret_str = ""
    diff = num1 - num2
    if diff == 0:
        # print("G")
        ret_str = data.GREEN
    elif diff > 0:
        if diff <= leeway:
            # print("Y, U")
            ret_str = data.YELLOW_UP
        else:
            # print("B, U")
            ret_str = data.BLACK_UP
    else:
        if diff >= -leeway:
            # print("Y, D")
            ret_str = data.YELLOW_DOWN
        else:
            # print("B, D")
            ret_str = data.BLACK_DOWN
    return ret_str



