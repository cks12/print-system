import requests
import shutil
from os import path
class Convert: 
    def __init__(self, zpl):
        self.zpl = zpl
        self.url = 'http://api.labelary.com/v1/printers/8dpmm/labels/4x2/'
        self.file = {"file":zpl}
        self.type = ""
        self.headers = ""
        
    def pdf(self): 
        self.headers = {'Accept' : 'application/pdf'} 
        self.type = "pdf"
        
    def epl(self):
        self.headers = {'Accept' : 'application/epl'} 
        self.type = "epl"

    def save__ZPL(self, name):
        _name = name
        self.type = "zpl"
        savePath = f"labels/Ro:{_name}.{self.type}"
        file = open(savePath, 'w')
        file.write(self.zpl)
        return path.join(path.dirname(savePath), f'Ro:{name}')

    def request(self, name):
        response = requests.post(self.url, headers=self.headers, files= self.file, stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True
            savePath = f"labels/Ro:{name}.{self.type}"
            with open(f'labels/Ro:{name}.{self.type}', 'wb') as out_file: 
                shutil.copyfileobj(response.raw, out_file)
                return path.join(path.dirname(savePath), f'Ro:{name}')
            
        else:
            print('Error: ' + response.text)
