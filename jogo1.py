
import random

print ("_____________________________________\n")
print ("///    Jogo de adivinhação       ///")
print ("//         Luiz Felipe            //")
print ("///   Bem vindo ao meu jogo      ///")
print ("_____________________________________")

numeroSecreto = random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("     Qual níveis de dificuldade?  ")
print(" (1)- Fácil (2)- Médio (3)- Difícil")

nivel = int(input("Escolha um nível:  "))

if(nivel == 1):
    print("20 tentativas")
    totalTentativas = 20
elif (nivel == 2):
    print("10 tentativas")
    totalTentativas = 10
elif(nivel == 3):
    print("5 tentativas")
    totalTentativas = 5
else:
    print("numero invalido")


for rodada in range (1, totalTentativas +1):
    print("Tentativa {} de {}".format(rodada,totalTentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
       print("Número invalido")
       continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if(acertou):
        print(f"Você acertou e fez {pontos}! ")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o numero secreto")
        pontosPerdidos = abs(numeroSecreto - chute)
        pontos = pontos - pontosPerdidos
            
print("Fim de jogo ! O número era ",numeroSecreto)