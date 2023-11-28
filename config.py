import json
#
#                                                           _   
#                                                          | |  
#     __      ___   _ _ __   ___ ___  _ __  _ __   ___  ___| |_ 
#     \ \ /\ / / | | | '_ \ / __/ _ \| '_ \| '_ \ / _ \/ __| __|
#      \ V  V /| |_| | | | | (_| (_) | | | | | | |  __/ (__| |_ 
#       \_/\_/  \__, |_| |_|\___\___/|_| |_|_| |_|\___|\___|\__|
#                __/ |                                          
#               |___/                                           
#
# TODOS OS DIREITOS RESERVADOS    
def ler_ou_criar_configuracao(nome_arquivo, valores_padrao):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            configuracao = json.load(arquivo)
            print(f'Configuração lida do arquivo "{nome_arquivo}".')
    except FileNotFoundError:
        configuracao = valores_padrao
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(configuracao, arquivo, indent=4)
            print(f'Arquivo de configuração "{nome_arquivo}" criado com valores padrão.')
    return configuracao