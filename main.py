import asyncio
import socketio
import json
import os 
import platform
from convert.main import Convert
from config import ler_ou_criar_configuracao

s = '''
 __        __                                           _   
 \ \      / /   _ _ __   ___ ___  _ __  _ __   ___  ___| |_ 
  \ \ /\ / / | | | '_ \ / __/ _ \| '_ \| '_ \ / _ \/ __| __|
   \ V  V /| |_| | | | | (_| (_) | | | | | | |  __/ (__| |_ 
    \_/\_/  \__, |_| |_|\___\___/|_| |_|_| |_|\___|\___|\__|
            |___/

Todos os direitos reservados @ WYNTECH LTDA
Suporte caio.souza@wyntech.inf.br
'''


def verificar_ou_criar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f'Diretório "{diretorio}" criado com sucesso.')
    else:
        print(f'Diretório "{diretorio}" já existe.')

sio = socketio.AsyncClient()
@sio.event
async def connect():
    print('Conexão feita com sucesso ao servidor!')
    await set_id("TEST-123")

def msg(e): {
    print(e)
}

@sio.event
async def conn(data):
    print(data)

def makeAFile(data):
    pass

@sio.event
async def makeAPrint(data):
    type = data["type"]
    _Conver = Convert(data["data"])
    ro = data["ro"]
    print(f"Imprimindo eitqueta do romaneio: {ro}")
    name = ""
    if type == "pdf":
        _Conver.pdf()
    
    elif type == "epl":
        _Conver.epl()        
    
    elif type == "img":
        _Conver.img()

    elif type == "zpl":
        name = _Conver.save__ZPL(data["ro"])
        name = f'{name}.{type}'
        if platform.system() == "Windows":
            from system.windows import printer
            printer(name)
        elif platform.system() == "Linux":
            from system.linux import printer
            printer(name, configuracao["LINUX_PRINT_NAME"])
        return
    
    name = _Conver.request(data["ro"])
    name = f'{name}.{type}'
    if platform.system() == "Windows":
        print("teste")
        from system.windows import printer
        printer(name)
    elif platform.system() == "Linux":
        from system.linux import printer
        printer(name, configuracao["LINUX_PRINT_NAME"])
@sio.event 
async def set_id(id):
    print(id)
    j = {}
    j["id"] = id
    print()
    await sio.emit("setid",json.dumps(j))

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('https://wyn-printer-system.azurewebsites.net/')
    print("> Conectando ao servidor python")
    await sio.wait()

if __name__ == '__main__':
    print(s)
    name = os.environ.get("USERNAME")
    system = platform.system()
    nome_arquivo_config = 'config.json'
    valores_padrao_config = {
        "ID":"IDENTIFICACÃO NO WYNPRINTSYSTEM",
        "LINUX_PRINT_NAME":"NOME DA IMPRESSORA, APENAS PARA LINUX"
    }
    configuracao = ler_ou_criar_configuracao(nome_arquivo_config, valores_padrao_config)
    print(f"Hostname: {name}")
    print(f"System: {system}")
    asyncio.run(main())
