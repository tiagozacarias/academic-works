#!/usr/bin/env python3
# coding=UTF-8
# Author: Tiago Eduardo Zacarias
# Version: 1.0
# Date: 21-05-2022
# License: GPLv3

# Variaveis

# Lista para recebimento de valores do tipo float
valores = []


# Functions

def id_pessoal():

    print(f"Bem Vindo a Lanchonete do Otavio Augusto")

# Função Cardápio
def cardapio():

    print(f"""

*************************Cardápio**********************         
| Código |              Descrição            | Valor  |        
|  100   |          Cachorro Quente          |R$9,00  | 
|  101   |          Cachorro Quente Duplo    |R$11,00 |
|  102   |          X-Egg                    |R$12,00 | 
|  103   |          X-Salada                 |R$13,00 | 
|  104   |          X-Bacon                  |R$14,00 | 
|  105   |          X-Tudo                   |R$17,00 | 
|  200   |          Refrigenrante Lata       |R$5,00  | 
|  201   |          Chá Gelado               |R$4,00  | 
******************************************************    
    """)

# Função Soma
def soma(x):

    print("""Deseja pedir mais alguma coisa?

1 - Sim

0 - Não

""")

    opcao = int(input())
    valores.append(x)

    if opcao > 1:

        print("Opção Inválida")

    elif opcao == 1:

        processar_cardapio()

    elif opcao == 0:

        list_sum = sum(number for number in valores)
        print(
            f"\033[0;32m[Valor total a ser pago é: R$ %.2f ]\033[0m" % (list_sum))

# Função Processar Cardapio (SWITCH)
def processar_cardapio():

        codigo = int(input("Entre com o Código Desejado:"))

        while codigo:

            if codigo == 100:

                x = 9

                print("Você pediu um Cachorro-Quente no Valor de R$9,00")

                soma(x)
      
                break

            elif codigo == 101:

                x = 11

                print("Você pediu um Cachorro-Quente Duplo no Valor de R$11,00")

                soma(x)
      
                break

            elif codigo == 102:

                x = 12

                print("Você pediu um X-Egg no Valor de R$12,00")

                break

            elif codigo == 103:

                x = 12

                print("Você pediu um X-Salada no Valor de R$12,00")

                soma(x)
      
                break

            elif codigo == 104:

                x = 14

                print("Você pediu um X-Bacon no Valor de R$14,00")

                soma(x)
      
                break

            elif codigo == 105:

                x = 17

                print("Você pediu um X-Tudo no Valor de R$17,00")

                soma(x)
      
                break

            elif codigo == 200:

                x = 5

                print("Você pediu um Refrigerante Lata no Valor de R$5,00")

                soma(x)
      
                break

            elif codigo == 201:

                x = 4

                print("Você pediu um Chá Gelado no Valor de R$4,00")

                soma(x)
      
                break
    
            else:
                
                print(f"Opção Invalida")
                processar_cardapio()
                continue


id_pessoal()
cardapio()
processar_cardapio()

