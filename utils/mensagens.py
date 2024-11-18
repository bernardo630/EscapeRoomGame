import time

def exibir_mensagem(mensagem):
    for linha in mensagem.split("\n"):
        print(linha)
        time.sleep(1)
    print("\n")
