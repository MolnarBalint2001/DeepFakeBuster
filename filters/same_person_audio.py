from filters.common import BaseAuthFilter
import torchaudio
from pyannote.audio import Pipeline
from moviepy.editor import VideoFileClip
import time
import torch
import uuid

import os
class SamePersonAudioFilter(BaseAuthFilter):
    
    
    def __init__(self, video_input) -> None:
        
        self.pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token="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")
        self.pipeline.to(torch.device(0))
        super().__init__(video_input, uuid.uuid4())
        


    def enhance_audio(self):
        from speechbrain.pretrained import SepformerSeparation as separator
        import torchaudio

        model = separator.from_hparams(source="speechbrain/sepformer-wham-enhancement", 
                                       savedir='pretrained_models/sepformer-wham-enhancement',
                                       run_opts={"device":"cuda"})
        # for custom file, change path
        est_sources = model.separate_file(path='tmp.wav') 

        torchaudio.save(f"{self.guid}_enhanced.wav", est_sources[:, :, 0].detach().cpu(), 8000)



    def run(self): 
        t1 = time.time()
        vv = VideoFileClip(self.video_input)
        file_name = f"{self.guid}.wav"
        vv.audio.write_audiofile(file_name)
        
        #self.enhance_audio()
        
        waveform, sample_rate = torchaudio.load(file_name)

        diarization = self.pipeline({"waveform": waveform, "sample_rate": sample_rate})
    
        print(len(diarization), "speaker")
        
        d  = time.time() - t1
        print(d, "s")
        os.remove(os.path.join(file_name))
        
        
    
    
if __name__ == "__main__":
    files = ["../assets/hackathon_files-20231124T182243Z-001/VID_20231124_191202.mp4",
                "../assets/hackathon_files-20231124T182243Z-001/VID_20231124_191232.mp4",
             "../assets/hackathon_files-20231124T182243Z-001/VID_20231124_191304.mp4",
             "../assets/hackathon_files-20231124T182243Z-001/VID_20231124_191318.mp4",
             ]
    
    for file in files:
            
        ff = SamePersonAudioFilter(file)
        
        ff.run()