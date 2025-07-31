
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
    print("20 tentativas! Ta com medo, frango 🤣")
elif(nivel == 2):
    print(" 10 tentativas! Ta com pouca coragem 🤣")
elif(nivel == 3):
    print(" 5 tentativas! Ta corajoso demais pro meu gosto 😱 ")
