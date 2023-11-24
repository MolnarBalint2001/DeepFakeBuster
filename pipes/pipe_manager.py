
from typing import List
from filters.common.base_auth_filter import BaseAuthFilter


class PipeManager:



    def __init__(self) -> None:
        self.pipes: List[BaseAuthFilter] = []
    
    
    
    def add_filter(self, filterPolicy:BaseAuthFilter):
        self.pipes.append(filterPolicy)
        
        return self
    
    
    def run_pipes(self):
        
        
        for pipe in self.pipes:
            pipe.run()
        