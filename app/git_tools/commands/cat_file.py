import os 
import zlib
from .base import BaseCommand 

class CatFileCommand(BaseCommand):
    
    def execute(self):
        flag = self.flag
        commitSHA = self.commitSHA
        
        if flag == "-p":
            folder = commitSHA[:2]
            file = commitSHA[2:]
            path_to_file = os.path.join(os.getcwd(),'.git','objects',folder)
            
            if not os.path.exists(path_to_file):
                raise ValueError(f"Not a valid object name {commitSHA}")
            
            with open(path_to_file,'rb') as f:
                compressed_data = f.read()
                decompressed_data = zlib.decompress(compressed_data)
                print(decompressed_data.decode())
        else:
            print('Invalid flag')

            
                    
        
        