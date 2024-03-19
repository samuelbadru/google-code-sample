"""A video player class."""

from .video_library import VideoLibrary
from .video_state import VideoState
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_state = VideoState("STOPPED", "")
        self._playlist_library = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        all_videos = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)

        print("Here's a list of all available videos:")
        for video in all_videos:
            tags = video.tags
            formatted_tags = ""

            for tag in tags:
                formatted_tags += tag + " "

            print(f"  {video.title} ({video.video_id}) [{formatted_tags.rstrip()}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id)

        if video is None:
            print("Cannot play video: Video does not exist")
        elif self._video_state.state == "STOPPED":
            print(f"Playing video: {video.title}")
            self._video_state.state = "PLAYING"
            self._video_state.video_id = video_id
        else:
            prev_video_id = self._video_state.video_id
            prev_video = self._video_library.get_video(prev_video_id)
            print(f"Stopping video: {prev_video.title}")
            print(f"Playing video: {video.title}")
            self._video_state.state = "PLAYING"
            self._video_state.video_id = video_id

    def stop_video(self):
        """Stops the current video."""

        if self._video_state.state == "PLAYING" or self._video_state.state == "PAUSED":
            video_id = self._video_state.video_id
            video = self._video_library.get_video(video_id)
            print(f"Stopping video: {video.title}")
            self._video_state.state = "STOPPED"
        elif self._video_state.state == "STOPPED":
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        random_vid = random.choice(self._video_library.get_all_videos())
        self.play_video(random_vid.video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self._video_state.state == "PLAYING":
            video_id = self._video_state.video_id
            video = self._video_library.get_video(video_id)
            print(f"Pausing video: {video.title}")
            self._video_state.state = "PAUSED"
        elif self._video_state.state == "PAUSED":
            video_id = self._video_state.video_id
            video = self._video_library.get_video(video_id)
            print(f"Video already paused: {video.title}")
        elif self._video_state.state == "STOPPED":
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._video_state.state == "PAUSED":
            video_id = self._video_state.video_id
            video = self._video_library.get_video(video_id)
            print(f"Continuing video: {video.title}")
            self._video_state.state = "PLAYING"
        elif self._video_state.state == "PLAYING":
            print("Cannot continue video: Video is not paused")
        elif self._video_state.state == "STOPPED":
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self._video_state.state == "STOPPED":
            print("No video is currently playing")
            return

        video_id = self._video_state.video_id
        video = self._video_library.get_video(video_id)
        tags = video.tags
        formatted_tags = ""

        for tag in tags:
            formatted_tags += tag + " "

        if self._video_state.state == "PLAYING":
            print(f"Currently playing: {video.title} ({video.video_id}) [{formatted_tags.rstrip()}]")
        elif self._video_state.state == "PAUSED":
            print(f"Currently playing: {video.title} ({video.video_id}) [{formatted_tags.rstrip()}] - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        duplicate_playlist = self.duplicate_playlist_check(playlist_name)

        if duplicate_playlist:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist_library.append(Playlist(playlist_name))
            print(f"Successfully created new playlist: {playlist_name}")

    def duplicate_playlist_check(self, playlist_name):
        duplicate_name = False
        for playlist in self._playlist_library:
            if playlist.name.lower() == playlist_name.lower():
                duplicate_name = True
        return duplicate_name

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """



        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
