import subprocess
import os 

def printer(file: str, _LINUX_ONLY_PRINTER_NAME_):
    sep_tup = os.path.splitext(file) 
    ext = sep_tup[1] 
    _file = sep_tup[0] 
    args = []
    path = os.getcwd()
    file= f'{path}/{file}'
    print(file)
    print(file, _LINUX_ONLY_PRINTER_NAME_)
    if ext == ".zpl":
        args = [
            'lp', '-d',
            _LINUX_ONLY_PRINTER_NAME_, '-o'
            'raw', file,
        ]
    
    elif ext == '.pdf':
        args = [
            'lp', '-d',
            _LINUX_ONLY_PRINTER_NAME_,file]
        
    elif ext == '.epl':
        args = [
            'lp', '-d',
            _LINUX_ONLY_PRINTER_NAME_,file]    
    subprocess.call(args)
    