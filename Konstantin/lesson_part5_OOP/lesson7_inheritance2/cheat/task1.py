# Напишите класс MusicAlbum, у которого есть:
#
# Атрибуты title, artist, release_year, genre, tracklist (название, исполнитель, год выхода, жанр, список треков.
# Метод play_random_track() для вывода случайного названия песни.


# Пример работы:
#
# Название: Deutschland
# Исполнитель: Rammstein
# Год: 2019
# Жанр: Neue Deutsche Härte
# Треки: ['Deutschland', 'Radio', 'Zeig dich', 'Ausländer', 'Sex', 'Puppe', 'Was ich liebe', 'Diamant', 'Weit weg', 'Tattoo', 'Hallomann']
# Воспроизводится трек 7: Was ich liebe

import random


class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_track(self, track_number):
        print(f"Воспроизводится трек  {track_number}: {self.tracklist[track_number - 1]}")

    def play_random_track(self):
        track_number = random.randint(1, len(self.tracklist))
        self.play_track(track_number)