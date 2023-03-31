from song import Song


class Album:
    def __init__(self, name: str):  # TODO might receive one or more song
        self.name = name
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song}. It's a single"
        if self.published:  # TODO if it is true or false
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in self.songs:
            return "Song is not in the album."
        if self.published:  # TODO if it is true or false
            return "Cannot remove songs. Album is published."

        self.songs.remove(song_name)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:  # TODO if it is true or false
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        song_info = "\n".join(["== " + song.get_info() for song in self.songs])
        return f'Album {self.name}\n' \
               f'{song_info}'


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
