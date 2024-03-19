"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name, video_id):
        self._name = name
        self._video_id = video_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, new_video_id):
        self._video_id = new_video_id
