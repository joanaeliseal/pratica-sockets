import socket
from pathlib import Path

HOST = '127.0.0.1'
PORT = 5000

servidor = (HOST, PORT)

print('=== Cliente ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def menu():
    print("Menu:")
    print("1 - Mostrar conteúdo do diretório")
    print("2 - Criar diretório")
    print("3 - Excluir diretório")
    print("4 - Mostrar arquivo")

def trata_opcoes(opcao_digitada):
    # 1 /tmp
    operacao, caminho = opcao_digitada.split(sep='/-/')
    caminho = Path(caminho)

    msg = ''
    resp = ''
    # Realiza a ação correspondente à opção do usuário
    if opcao == "LERDIR":
        # Mostra o conteúdo do diretório atual
        print('LERDIR/-/'+ str(caminho))
        for arquivo in caminho.interdir():
            resp += str(arquivo) + '\n'
    
    elif opcao == "CRIARDIR":
        # Cria um novo diretório
        print('CRIARDIR/-/'+ str(caminho))
        caminho.mkdir(parents=True, exist_ok=True)
        resp += f'\nPasta {caminho} criada com sucesso!\n'
        
    elif opcao == "EXCLUIRDIR":
        # Exclui um diretório
        print('EXCLUIRDIR/-/'+ str(caminho))
        caminho.rmdir()
        resp += f'\nPasta {caminho} removida com sucesso!\n'
        
    elif opcao == "MOSTRAR":
        # Mostra o conteúdo de um arquivo
        print('MOSTRAR/-/'+ str(caminho))
        resp += f'\Lendo de {caminho}:\n'
        resp += str(caminho.read_text())
    
    return resp

while True:
    msg, cliente = udp.recvfrom(1024)
    res = trata_opcoes(msg.decode())
    print('Recebi de', cliente, 'a mensagem', msg.decode())
    menu()
    opcao = input('')
    msg = trata_opcoes(opcao)
    udp.sendto(msg.encode(encoding="utf-8"), servidor)
    resposta_servidor, s = udp.recvfrom(1024)
    print(resposta_servidor.decode(encoding='utf-8', errors='backslashreplace'))
