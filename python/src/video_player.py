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
        self.print_video_details(all_videos)

    def print_video_details(self, all_videos):
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

        duplicate_playlist = self.check_playlist_exists(playlist_name)

        if duplicate_playlist:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlist_library.append(Playlist(playlist_name))
            print(f"Successfully created new playlist: {playlist_name}")

    def check_playlist_exists(self, playlist_name):
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

        valid_playlist = self.check_playlist_exists(playlist_name)
        if not valid_playlist:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return

        video = self._video_library.get_video(video_id)
        if video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return

        duplicate_video = self.duplicate_playlist_video(playlist_name, video_id)
        if duplicate_video:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return

        video_name = self._video_library.get_video(video_id).title
        print(f"Added video to {playlist_name}: {video_name}")

    def duplicate_playlist_video(self, playlist_name, video_id):
        for playlist in self._playlist_library:
            if playlist.name.lower() == playlist_name.lower():
                videos = playlist.videos

                for video in videos:
                    if video.video_id == video_id:
                        return True

                playlist.videos = self._video_library.get_video(video_id)
                return False

    def show_all_playlists(self):
        """Display all playlists."""

        if not self._playlist_library:
            print("No playlists exist yet")
            return

        all_playlists = sorted(self._playlist_library, key=lambda playlist: playlist.name)

        print("Showing all playlists:")
        for playlist in all_playlists:
            print(f"  {playlist.name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for playlist in self._playlist_library:
            if playlist.name.lower() == playlist_name.lower():
                print(f"Showing playlist: {playlist_name}")
                videos = playlist.videos

                if not videos:
                    print("  No videos here yet")
                    return
                else:
                    self.print_video_details(videos)
                    return

        print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_exists = False

        video = self._video_library.get_video(video_id)

        if not video:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return

        for playlist in self._playlist_library:
            if playlist.name.lower() == playlist_name.lower():
                playlist_exists = True
                videos = playlist.videos

                for video in videos:
                    if video.video_id == video_id:
                        playlist.delete_video(video_id)
                        print(f"Removed video from {playlist_name}: {video.title}")
                        return

        if not playlist_exists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = False

        for playlist in self._playlist_library:
            if playlist.name.lower() == playlist_name.lower():
                playlist_exists = True
                playlist.clear()
                print(f"Successfully removed all videos from {playlist_name}")

        if not playlist_exists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        for playlist in self._playlist_library:
            if playlist.name.lower() == playlist_name.lower():
                self._playlist_library.remove(playlist)
                print(f"Deleted playlist: {playlist_name}")
                return

        print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)

        video_results = []

        for video in videos:
            if search_term.lower() in video.title.lower():
                video_results.append(video)

        if not video_results:
            print(f"No search results for {search_term}")
            return

        self.print_video_details_search(video_results, search_term)

        command = input()

        try:
            index = int(command) - 1

            if index in range(len(video_results)):
                selected_video = video_results[index]
                self.play_video(selected_video.video_id)
        except ValueError:
            return

    def print_video_details_search(self, all_videos, query):
        print(f"Here are the results for {query}:")
        index = 1
        for video in all_videos:
            tags = video.tags
            formatted_tags = ""

            for tag in tags:
                formatted_tags += tag + " "

            print(f"{index}) {video.title} ({video.video_id}) [{formatted_tags.rstrip()}]")
            index += 1
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")






    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        if "#" not in video_tag:
            print(f"No search results for {video_tag}")
            return

        videos = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)

        video_results = []

        for video in videos:
            for tag in video.tags:
                if video_tag.lower() in tag.lower():
                    video_results.append(video)


        if not video_results:
            print(f"No search results for {video_tag}")
            return

        self.print_video_details_search(video_results, video_tag)

        command = input()

        try:
            index = int(command) - 1

            if index in range(len(video_results)):
                selected_video = video_results[index]
                self.play_video(selected_video.video_id)
        except ValueError:
            return

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


# TODO Refactor the multiple helper functions that all locate the playlist. Dictionary may be better than list, or playlist class to have a locate function
