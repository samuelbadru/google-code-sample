class VideoState:
    def __init__(self, state, video_id):
        self._state = state
        self._video_id = video_id

    @property
    def state(self):
        return self._state

    @property
    def video_id(self):
        return self._video_id
