from utils.mensagens import exibir_mensagem

def enigma_codigo():
    exibir_mensagem("Enigma do Código: Decifre o código escondido nas palavras.")
    dica = "O código está nas iniciais das palavras: 'Casa Amarela Perto da Escola Rosa'."
    exibir_mensagem(f"Dica: {dica}")
    codigo_correto = "CAPER"

    while True:
        resposta = input("Digite o código: ").upper()
        if resposta == codigo_correto:
            exibir_mensagem("Você decifrou o código! Parabéns.")
            return True
        else:
            exibir_mensagem("Código incorreto. Tente novamente!")
