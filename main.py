



from pipe_manager.pipe_manager import PipeManager
from glob import glob

from threading import Thread
from multiprocessing import Process
from typing import List
from filters.same_person_audio import SamePersonAudioFilter
from time import time
def validate_video(video_path: str):
    pipe_manger = PipeManager(video_input=video_path) \
                .add_filter(SamePersonAudioFilter)
    
    pipe_manger.run_pipes()
    pass




def main():
    
    
    pipe_manager_threads: List[Thread] = []
    
    t = time()
    print("PipeManger started running...")
    print("------------------------------\n")
    for path in glob("./assets/hackathon_files-20231124T182243Z-001/*.mp4"):
        mg_th = Thread(target=validate_video, args=(path,))
        mg_th.daemon = True
        mg_th.start()
        pipe_manager_threads.append(mg_th)
        
    print("Waiting to finish all the pipes!")
    
    for th in pipe_manager_threads:
        th.join()
    
    
    d = time() - t
    print(f"Everything run under {d:0.2f} s")
    
    
    
        

    
    
    pass



if __name__ == "__main__":
    print("Started!")
    main()
    pass