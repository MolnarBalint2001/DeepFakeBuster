
from typing import List
from filters.common.base_auth_filter import BaseAuthFilter
from time import time
from threading import Thread
class PipeManager:

    def __init__(self,video_input) -> None:
        self.video_input = video_input
        self.pipes: List[BaseAuthFilter] = []
    
    
    
    def add_filter(self, filter_class):
        
        filter_policy = filter_class(self.video_input)
        self.pipes.append(filter_policy)
        
        return self
    
    
    def run_pipes(self):
        
        
        t1 = time()
        print("[*] Evaulating video: " + self.video_input)
        threads: List[Thread] = []
        for pipe in self.pipes:
            pipe_thread = Thread(target=pipe.run, args=(), daemon=True)
            threads.append(pipe_thread)
            
        try:
            for th in threads:
                th.start()
                
            for th in threads:
                th.join()
        except Exception as e:
            print("Authorization failed!", e)
        finally:
            delta = time() - t1
            print("----------------------------------")
            print(f"Video evaulation ran under: {delta:0.2f}s")
        
