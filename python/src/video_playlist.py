"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name):
        self._name = name
        self._videos = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def videos(self):
        return self._videos

    @videos.setter
    def videos(self, video):
        self._videos.append(video)

    def delete_video(self, video_id):
        for video in self._videos:
            if video.video_id == video_id:
                self._videos.remove(video)
                return

    def clear(self):
        self._videos.clear()