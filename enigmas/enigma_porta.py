from utils.mensagens import exibir_mensagem

def enigma_porta():
    exibir_mensagem("Enigma da Porta: Digite a sequência correta para abrir a porta.")
    exibir_mensagem("A dica é: 'O vento sopra para cima, gira à direita e desce ao chão.'")
    sequencia_correta = ['cima', 'direita', 'baixo']
    
    while True:
        tentativa = input("Digite os movimentos na sequência, separados por vírgulas (ex: cima,baixo,direita): ").lower().split(',')
        if tentativa == sequencia_correta:
            exibir_mensagem("Incrível! Você abriu a porta.")
            return True
        else:
            exibir_mensagem("Sequência incorreta. Tente novamente!")
