from utils.mensagens import exibir_mensagem

def enigma_cofre():
    exibir_mensagem("Enigma do Cofre: Encontre a soma correta dos números ocultos no texto.")
    texto = "O texto diz: 'Os números mágicos são 7, 15 e 10. Somando-os, você abrirá o cofre.'"
    exibir_mensagem(texto)
    resposta_correta = 7 + 15 + 10
    
    while True:
        try:
            resposta = int(input("Digite a soma dos números: "))
            if resposta == resposta_correta:
                exibir_mensagem("Parabéns! Você abriu o cofre.")
                return True
            else:
                exibir_mensagem("Resposta incorreta. Tente novamente!")
        except ValueError:
            exibir_mensagem("Entrada inválida. Digite apenas números.")
