import json

def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton(*args, **kw):  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  

@singleton
class configData():
    
    def __init__(self, file):
        config_file = open(file, 'r')
        config_text = config_file.read()     
        self.data = json.loads(config_text)
        config_file.close() 
