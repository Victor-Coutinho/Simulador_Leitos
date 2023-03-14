import time
import random
from Estrutura import paciente,leito
from Fila import fila


#---------------------- filas usadas no programa--------------------------------
entrandop = fila() #entrada dos pacientes
entrandol = fila() #entrada dos leitos
grave3A = fila()
grave4A = fila()
grave5A = fila()
grave3P = fila()
grave4P = fila()
grave5P = fila()
grave3N = fila()
grave4N = fila()
grave5N = fila()
leitoA = fila()
leitoP = fila()
leitoN = fila()


#---------------------criando e inserindo os pacientes e os leitos em listas-------------------
rotacoes = 0
while rotacoes < 5:
    print("Pacientes Chegando...")
    print("Leitos Chegando...")
    time.sleep(5)

    quantidadep = random.randint(1,100)
    quantidadel = random.randint(1,100)

    for i in range(quantidadep):
        pessoa = paciente(i)
        entrandop.insere(pessoa.resultado)

    totalP = entrandop.tamanho

    for i in range(quantidadel):
        vagas = leito(i)
        entrandol.insere(vagas.resultado)

    totalL = entrandol.tamanho
    
    print("-" * 10)
    print(f"Total de pacientes:{totalP}")
    print(f"Total de leitos:{totalL}")
    print("-" * 10)
    time.sleep(5)
    #-----------------------------------------------------------------------------------------
        
    # Inserindo os pacientes nas suas respectivas filas, seguindo idade e gravidade
    for i in range(entrandop.tamanho):
        ponteiro = entrandop.primeiro.__dado__
        if ponteiro[0] == '3' and ponteiro[1] == "0" :
            grave3N.insere(ponteiro)
        elif ponteiro[0] == '4' and ponteiro[1] == "0" :
            grave4N.insere(ponteiro)
        elif ponteiro[0] == '5' and ponteiro[1] == "0" :
            grave5N.insere(ponteiro)
        elif ponteiro[0] == '3' and ponteiro[1] == "1" :
            grave3P.insere(ponteiro)
        elif ponteiro[0] == '4' and ponteiro[1] == "1" :
            grave4P.insere(ponteiro)
        elif ponteiro[0] == '5' and ponteiro[1] == "1" :
            grave5P.insere(ponteiro)
        elif ponteiro[0] == '3' and ponteiro[1] == "2" :
            grave3A.insere(ponteiro)
        elif ponteiro[0] == '4' and ponteiro[1] == "2" :
            grave4A.insere(ponteiro)
        elif ponteiro[0] == '5' and ponteiro[1] == "2" :
            grave5A.insere(ponteiro)

        entrandop.remove()

    # Separando os leitos Neonatais dos Pediatricos e dos Adultos
    for i in range(entrandol.tamanho):
        ponteiro =  entrandol.primeiro.__dado__
        
        if ponteiro[0] == '0':
            leitoN.insere(ponteiro)
        elif ponteiro[0] == '1':
            leitoP.insere(ponteiro)
        elif ponteiro[0] == '2':
            leitoA.insere(ponteiro)
        
        entrandol.remove()
    #------------------------------- Prints do Terminal--------------------------------------
    print("-" * 10)
    print("Leitos:")
    print(f"Total de Leitos para Adultos:  {leitoA.tamanho}")
    print(f"Total de Leitos para Crianças: {leitoP.tamanho}")
    print(f"Total de Leitos para Neonatal: {leitoN.tamanho}")
    print("-" * 10)
    print("Adultos:")
    print(f"Emergência: {grave5A.tamanho}  Muito Urgente: {grave4A.tamanho}  Urgente:  {grave3A.tamanho}")
    print("Crianças:")
    print(f"Emergência: {grave5P.tamanho}  Muito Urgente: {grave4P.tamanho}  Urgente: {grave3P.tamanho}")
    print("Neonatal:")
    print(f"Emergência: {grave5N.tamanho}  Muito Urgente: {grave4N.tamanho}  Urgente: {grave3N.tamanho}")
    print("-" * 10)
    time.sleep(10)

    #-------------------------- Algoritimo de remoção das filas --------------------------------
    for i in range(leitoN.tamanho):
        if grave5N.tamanho > 0:
            grave5N.remove()
            leitoN.remove()
        elif grave4N.tamanho > 0:
            grave4N.remove()
            leitoN.remove()
        elif grave3N.tamanho > 0:
            grave3N.remove()
            leitoN.remove()
        else:
            break

    for i in range(leitoP.tamanho):
        if grave5P.tamanho > 0:
            grave5P.remove()
            leitoP.remove()
        elif grave4P.tamanho > 0:
            grave4P.remove()
            leitoP.remove()
        elif grave3P.tamanho > 0:
            grave3P.remove()
            leitoP.remove()
        else:
            break


    for i in range(leitoA.tamanho):
        if grave5A.tamanho > 0:
            grave5A.remove()
            leitoA.remove()
        elif grave4A.tamanho > 0:
            grave4A.remove()
            leitoA.remove()
        elif grave3A.tamanho > 0:
            grave3A.remove()
            leitoA.remove()
        else:
            break
    #------------------------------ Print no Terminal---------------------
    print("Alocando Pacientes nos Leitos...")
    time.sleep(5)
    print("-" * 10)
    print("Leitos:")
    print(f"Total de Leitos para Adultos:  {leitoA.tamanho}")
    print(f"Total de Leitos para Crianças: {leitoP.tamanho}")
    print(f"Total de Leitos para Neonatal: {leitoN.tamanho}")
    print(f"Leitos no Total:{leitoA.tamanho + leitoP.tamanho + leitoN.tamanho}")
    print("-" * 10)
    print("Adultos:")
    print(f"Total: {grave5A.tamanho + grave4A.tamanho + grave3A.tamanho}")
    print(f"Fila para Emergência: {grave5A.tamanho}  Fila para Muito Urgente: {grave4A.tamanho}  Fila para Urgente: {grave3A.tamanho}")
    print("Crianças:")
    print(f"Total: {grave5P.tamanho + grave4P.tamanho + grave3P.tamanho}")
    print(f"Fila para Emergência: {grave5P.tamanho}  Fila para Muito Urgente: {grave4P.tamanho}  Fila para Urgente: {grave3P.tamanho}")   
    print("Neonatal:")
    print(f"Total: {grave5N.tamanho + grave4N.tamanho + grave3N.tamanho}")
    print(f"Fila para Emergência: {grave5N.tamanho}  Fila para Muito Urgente: {grave4N.tamanho}  Fila para Urgente: {grave3N.tamanho}")   
    print("-" * 10)
    time.sleep(10)

    rotacoes = rotacoes + 1




