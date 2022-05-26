#!/usr/bin/env python3
# coding=UTF-8
# Author: Tiago Eduardo Zacarias
# Version: 1.0
# Date: 21-05-2022
# License: GPLv3

# Listas globais para recebimento de valores do tipo inteiro

# Variáveis valores iniciais transitivos
vli_valores_peso = []
vli_comp_valores_rota = []
vli_valores_dimensao = []

# Variáveis valores finais
vlf_valores_dimensao = []
vlf_reais = []
vlf_valores_peso = []
vlf_comp_valores_rota = []

# Functions

def id_pessoal():

    print(f"Bem Vindo a Companhia de Logistica Otavio Augusto")

# Classes
class Principal:

    # Função Dimensão do Objeto.
    def dimensoesObjeto():

        # Input/Output de altura.

        while True:

            try:

                val_alt = int(input("Digite a altura do Objeto (em cm:)"))

                if val_alt >= 100000:

                    print(str.strip("""
                            Não aceitamos objetos com dimensões tão grandes\n
                            Entre com as dimenções desejadas novamente\n
                                    """))
                else:

                    vli_valores_dimensao.append(val_alt)

                    Principal.d1()

            except(UnboundLocalError, ValueError):

                print("Você digitou alguma dimensão com valor não numerico")

                Principal.dimensoesObjeto()

    def d1():

        while True:

            try:

                val_com = int(input("Digite o comprimento do Objeto (em cm:)"))

                if val_com >= 100000:

                    print(str.strip("""
                            Não aceitamos objetos com dimensões tão grandes\nEntre com as dimenções desejadas novamente\n
                                        """))
                else:

                    vli_valores_dimensao.append(val_com)

                    Principal.d2()

            except(UnboundLocalError, ValueError):

                print("Você digitou alguma dimensão com valor não numerico")

                Principal.d1()

    def d2():

        while True:

            try:

                val_lar = int(input("Digite o largura do Objeto (em cm:)"))

                if val_lar >= 100000:

                    print(str.strip(
                        """Não aceitamos objetos com dimensões tão grandes\nEntre com as dimenções desejadas novamente\n"""))

                else:

                    vli_valores_dimensao.append(val_lar)

            except(UnboundLocalError, ValueError):

                print("Você digitou alguma dimensão com valor não numerico")

                Principal.d2()

            try:
                # Calculo da dimensão (em cm3)
                list_sum = vli_valores_dimensao[0] * \
                    vli_valores_dimensao[1] * vli_valores_dimensao[2]
                vlf_valores_dimensao.append(list_sum)

                # Condicional dimensão versus valor
                if list_sum < 1000:

                    vlf_reais.append(10)

                elif list_sum >= 1000 and list_sum < 10000:

                    vlf_reais.append(20)

                elif list_sum >= 10000 and list_sum < 30000:

                    vlf_reais.append(30)

                elif list_sum >= 30000 and list_sum < 100000:

                    vlf_reais.append(50)

                else:

                    print("O volume do objeto é (em cm3): %.1f" %
                          (vlf_valores_dimensao[0]))
                    print(str.strip(
                        """Não aceitamos objetos com dimensões tão grandes\nEntre com as dimenções desejadas novamente\n"""))

                    # Remove valores da lista inical
                    vli_valores_dimensao.clear()
                    vlf_valores_dimensao.clear()

                    Principal.dimensoesObjeto()

                print("O volume do objeto é (em cm3): %.1f" %
                      (vlf_valores_dimensao[0]))

            except(UnboundLocalError, ValueError):

                print("Você digitou alguma dimensão com valor não numerico")

            Principal.pesoObjeto()

    # Função Peso

    def pesoObjeto():

        while True:

            try:

                peso = int(input("Digite o peso do Objeto (em kg:)"))

                if peso >= 30:

                    print(str.strip(
                        """Não aceitamos objetos tão pesados\nEntre com o peso desejado novamente\n"""))
                            
                    # Remove valores da lista inicial
                    vlf_valores_peso.clear()
                    vlf_valores_peso.clear()

                    Principal.pesoObjeto()

                else:

                    vli_valores_peso.append(peso)

                if peso <= 0.1:

                    pf = peso * 1

                    vlf_valores_peso.append(pf)

                elif peso > 0.1 and peso <= 1:

                    pf = peso * 1.5

                    vlf_valores_peso.append(pf)

                elif peso > 1 and peso <= 10:

                    pf = peso * 2

                    vlf_valores_peso.append(pf)

                else:

                    pf = peso * 3

                    vlf_valores_peso.append(pf)

            except(UnboundLocalError, ValueError):

                print("Você digitou peso com valor não numerico")
                Principal.pesoObjeto()

            Principal.rotaObjeto()

    # Função Rota objeto

    def rotaObjeto():

        while True:

            try:

                
                print("Selecione a rota:")
                print("BR - De Brasília para Rio de Janeiro")
                print("BS - De Brasília para São Paulo")
                print("RB - De Rio de Janeiro para Brasília")
                print("RS - De Rio de Janeiro para São Paulo")
                print("SR - De São Paulo para Rio de Janeiro")
                print("SB - De São Paulo para Brasília")       
                        

                rota = str(input("Digite a rota do Objeto:"))

                if rota != "br" and rota != "bs" and rota != "rb" and rota != "rs" and rota != "sr" and rota != "sb":

                    print(
                        """Você digitou uma rota que não existe\nPor Favor entre com a rota desejada novamente\n""")

                    Principal.rotaObjeto()

                elif rota == "br":

                    rt = vlf_reais[0] * vlf_valores_peso[0] * 1.5

                    print("Total a pagar(R$): %.2f" % (rt), end="  ")
                    print(
                        f"(\033[0;32m Dimensões:{vlf_valores_dimensao[0]} * Peso:{vlf_valores_peso[0]} * 1.5)\033[0m")

                elif rota == "bs":

                    rt = vlf_reais[0] * vlf_valores_peso[0] * 1.2

                    print("Total a pagar(R$): %.2f" % (rt), end="  ")
                    print(
                        f"(\033[0;32m Dimensões:{vlf_valores_dimensao[0]} * Peso:{vlf_valores_peso[0]} * 1.2)\033[0m")

                elif rota == "rb":

                    rt = vlf_reais[0] * vlf_valores_peso[0] * 1.5

                    print("Total a pagar(R$): %.2f" % (rt), end="  ")
                    print(
                        f"(\033[0;32m Dimensões:{vlf_valores_dimensao[0]} * Peso:{vlf_valores_peso[0]} * 1.5)\033[0m")

                elif rota == "rs":

                    rt = vlf_reais[0] * vlf_valores_peso[0] * 1

                    print("Total a pagar(R$): %.2f" % (rt), end="  ")
                    print(
                        f"(\033[0;32m Dimensões:{vlf_valores_dimensao[0]} * Peso:{vlf_valores_peso[0]} * 1)\033[0m")

                elif rota == "sr":

                    rt = vlf_reais[0] * vlf_valores_peso[0] * 1

                    print("Total a pagar(R$): %.2f" % (rt), end="  ")
                    print(
                        f"(\033[0;32m Dimensões:{vlf_valores_dimensao[0]} * Peso:{vlf_valores_peso[0]} * 1)\033[0m")

                elif rota == "sb":

                    rt = vlf_reais[0] * vlf_valores_peso[0] * 1.2

                    print("Total a pagar(R$): %.2f" % (rt), end="  ")
                    print(
                        f"(\033[0;32m Dimensões:{vlf_valores_dimensao[0]} * Peso:{vlf_valores_peso[0]} * 1.2)\033[0m")

            except(UnboundLocalError, ValueError):

                print(
                    """Você digitou parametros invalidos para rota\nPor Favor entre com a rota desejada novamente\n""")


id_pessoal()
Principal.dimensoesObjeto()
