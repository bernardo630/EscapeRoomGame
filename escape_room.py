from enigmas.enigma_cofre import enigma_cofre
from enigmas.enigma_porta import enigma_porta
from enigmas.enigma_codigo import enigma_codigo
from utils.mensagens import exibir_mensagem

def jogo_escape_room():
    exibir_mensagem("Bem-vindo ao Escape Room Virtual!\nVocê está trancado em uma sala misteriosa.")
    exibir_mensagem("Resolva os enigmas para escapar.")
    
    enigmas_resolvidos = 0
    
    # Resolver Enigma 1
    if enigma_cofre():
        enigmas_resolvidos += 1
    
    # Resolver Enigma 2
    if enigma_porta():
        enigmas_resolvidos += 1
    
    # Resolver Enigma 3
    if enigma_codigo():
        enigmas_resolvidos += 1
    
    # Final do jogo
    if enigmas_resolvidos == 3:
        exibir_mensagem("Parabéns! Você resolveu todos os enigmas e escapou da sala.")
    else:
        exibir_mensagem("Você não conseguiu resolver todos os enigmas. Tente novamente.")

if __name__ == "__main__":
    jogo_escape_room()
