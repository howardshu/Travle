from get_songs import songs, get_songs
import random


class Game:
    def __init__(self):
        self.guesses = 0
        self.solved = False
        self.target = random.choice(songs)
        # self.guessList = []

    def guess(self, song_guess):
        if self.guesses >= 8 or self.solved:
            return "", self.guesses, self.solved, None  # out of guesses or already solved

        song_hit = None
        # Search for the guessed song in the songs list
        for song in songs:
            if song.title == song_guess:
                song_hit = song
                song_found = True
                break
        if song_hit is None:
            return "", self.guesses, self.solved, None  # not found

        self.guesses += 1
        solved, stat_str = self.target.check_match(song_hit)
        # self.guessList.append((song_hit, stat_str))
        self.solved = solved
        return stat_str, self.guesses, self.solved, song_hit
