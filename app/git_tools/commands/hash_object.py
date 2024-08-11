import os 
import hashlib
import zlib
class HashObjectCommand:
    def __init__(self, flag, filePath):
        self.flag = flag 
        self.filePath = filePath
    
    
    def execute(self):
        filePath = os.path.abspath(self.filePath)
        if not os.path.exists(filePath):
            raise FileNotFoundError(f"could not open {self.filePath} for reading: No sucn file ")
        
        fileContent = os.read(filePath)
        fileLength = len(fileContent)
        header = f"blob ${fileLength}\0".encode()
        blob = header+fileContent
        hash_object = hashlib.sha1(blob)
        
        hash_hex = hash_object.hexdigest()
        
        if self.flag and self.flag  == '-w':
            folder = hash_hex[:2]
            file = hash_hex[2:]
            
            folderPath = os.path.join(os.getcwd(),'.vcs','objects',folder)
            
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
                
            
            compressed_data = zlib.compress(blob,level=0)
            
            with open(os.path.join(folderPath,file),'wb') as f:
                f.write(compressed_data)
            
        
        print(hash_object)
            
         