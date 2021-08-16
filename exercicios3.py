#Exercícios
#1) Gerar um número de 1 a 100, e solicitar para que o usuário tente adivinhar o número.
numero = range(1, 100)
teste = int(input("Digite o seu número:"))
print("Você digitou {}".format(teste))
if (numero == teste):
    print("Acertou!")
else:
    print("Errou!")

#2) Receba um endereço de e-mail, e faça um sistema que receba os dados do usuário.
usuario = input("Informe seu usuário:")
email = input("Informe seu e-mail:")
confirmacao = input("{}, confirme seu e-mail".format(usuario))
if(email == confirmacao):
    print("Seu e-mail está correto, {}!".format(usuario))
else:
    print("E-mail não identificado, tente novamente!")
senha = input("Crie uma senha:")
confirmacao1 = input("Confirme sua senha:")
if(senha == confirmacao1):
    print("Sua senha está correta {}!".format(usuario))
else:
    print("Senha incorreta, tente novamente!")
if((email == confirmacao) and (senha == confirmacao1)):
    print("Cadastro concluído!")
else:
    print("Alguma informação está errada, tente novamente!")

#Exercício Extra) Fazer uma lista com 100 palavras, e solicitar que o computador acerte a palavra, que foi escolhida pelo usuário.

import random

lista = ("bola", "casa", "maça", "caderno", "relógio", "coisa" , "tempo" , "ano" , "dia" , "homem" , "senhor" , "senhora" , "moço" , "moça" )
palavra = input("Digite uma palvra:")
palavra_Aleatoria = print(random.choice(lista))
if(palavra == palavra_Aleatoria):
    print("Você acertou!")
else:
    print("Você errou!")

