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
        print("savePath", savePath)
        try:
            out_file = open(savePath, 'w')
            out_file.write(self.zpl)
            out_file.close()
            return path.join(path.dirname(savePath), f'Ro:{name}')
        except:
            print("err")
    def print__zpl(self,name):
        import win32print
        import os
        _name = name
        sep_tup = os.path.splitext(name)
        default_printer_name = win32print.GetDefaultPrinter()
        hPrinter = win32print.OpenPrinter(default_printer_name)
        raw_data = bytes(self.zpl, 'utf-8')
        try:
            win32print.StartDocPrinter(
                hPrinter, 1, ("IMPRESSÃO WYNCONNECT", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, raw_data)
                win32print.EndPagePrinter(hPrinter)
            finally:
                    win32print.EndDocPrinter(hPrinter)
        finally:
                win32print.ClosePrinter(hPrinter)

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
