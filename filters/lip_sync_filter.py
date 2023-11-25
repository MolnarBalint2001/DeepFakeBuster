

from common import BaseAuthFilter
from wav2lip.Wav2Lip import Processor
from moviepy.editor import VideoFileClip


class LipSyncFilter(BaseAuthFilter):
    
    
    def __init__(self, video_input) -> None:
        super().__init__(video_input)
        
        
    def run(self):
        vv = VideoFileClip(self.video_input)
        
        vv.audio.write_audiofile("tmp_lipsync.wav")
        pass
    
    
if __name__ == "__main__":
    pass