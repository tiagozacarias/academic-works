#!/usr/bin/env python3
# coding=UTF-8
# Author: Otavio Augusto
# Version: 1.0
# Date: 21-05-2022
# License: GPLv3

# Functions 

def id_pessoal():

                print(f"Bem Vindo a Loja do Otavio Augusto")

def desconto():
              
                
                # Variaveis
                valor_produto = float(input("Entre com o Valor do Produto:")) 
                valor_quantidade = float(input("Entre com o Valor da Quantidade:"))
                valor_total = valor_produto * valor_quantidade
              
                    # Quantidade sem desconto
                if valor_quantidade <= 9:
                   
                    print("O valor sem desconto foi R$ %.2f" %(valor_produto * valor_quantidade), end="  ")
                    print(f"\033[0;32m[ Desconto: 0% ]\033[0m")

                    # Quantidade com desconto de 5%
                elif valor_quantidade >= 10 and valor_quantidade <= 99:

                    print("O valor sem desconto foi R$ %.2f" %(valor_total))
                    print("O valor com desconto foi R$ %.2f" %(valor_total - valor_total * 5 / 100), end="  ")
                    print(f"\033[0;32m[ Desconto: 5% ]\033[0m")
                
                     # Quantidade com desconto de 10%
                elif valor_quantidade >= 100 and valor_quantidade <= 999:
                    
                    print("O valor sem desconto foi R$ %.2f" %(valor_total))
                    print("O valor com desconto foi R$ %.2f" %(valor_total - valor_total * 10 / 100), end="  ")
                    print(f"\033[0;32m[ Desconto: 10% ]\033[0m")
               
                    # Quantidade com desconto de 15%
                else:
                
                    print("O valor sem desconto foi R$ %.2f" %(valor_total))
                    print("O valor com desconto foi R$ %.2f" %(valor_total - valor_total * 10 / 100), end="  ")
                    print(f"\033[0;32m[ Desconto: 15% ]\033[0m")

id_pessoal()
desconto()
