class VideoState:
    def __init__(self, state, video_id):
        self._state = state
        self._video_id = video_id

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, new_video_id):
        self._video_id = new_video_id
