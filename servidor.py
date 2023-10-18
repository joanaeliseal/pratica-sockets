import socket

HOST = '127.0.0.1'
PORT = 5000

print('=== Servidor ===')

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

def trata_opcoes(msg):
    # 1 /tmp
    valores = msg.split(sep=':')
    operacao = valores[0]
    caminho = valores[1]

    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt

    msg = ''
    # Realiza a ação correspondente à opção do usuário
    if operacao == "LERDIR":
        # Mostra o conteúdo do diretório atual
        print('LERDIR:' + caminho)
    elif operacao == "CRIARDIR":
        # Cria um novo diretório
        print('CRIARDIR:' + caminho)
    elif operacao == "EXCLUIRDIR":
        # Exclui um diretório
        print('EXCLUIRDIR:' + caminho)
    elif operacao == "MOSTRAR":
        # Mostra o conteúdo de um arquivo
        print('MOSTRAR:' + caminho)
    return msg

while True:
    msg, cliente = udp.recvfrom(1024)
    trata_opcoes(msg.decode())
    print('Recebi de', cliente, 'a mensagem', msg.decode(encoding="utf-8"))

    # mini protocolo
    # LERDIR:/tmp/
    # CRIARDIR:/tmp/eu
    # EXCLUIRDIR:/tmp/eu
    # MOSTRAR:/tmp/eu/proxima_prova.txt



    resposta = 'mensagem recebida com sucesso!'
    udp.sendto(resposta.encode(), cliente)
    print('Resposta enviada!')