#!/usr/bin/env python3
# coding=UTF-8
# Author: Tiago Eduardo Zacarias
# Version: 1.0
# Date: 21-05-2022
# License: GPLv3

# Variáveis valores iniciais transitivos
# Dicionarios
contador = [0]
cadastro_codigo = {}
cadastro_valor = {}
cadastro_nome_fab_peca = {}


def id_pessoal():

    print(f"Bem Vindo ao Controle de estoque da Bicicletaria do Otavio Augusto")

# Class Principal 
class principal:


    def buscar_codigo(val):
                    
        for chave, value in cadastro_codigo.items():

            if val == value:

                print(f"-------------------------\n")
                print(f"Código : {cadastro_codigo[chave]:03d}")
                print(f"Nome  : {chave}")                   
                print(f"Fabricante : {cadastro_nome_fab_peca[chave]}")                    
                print("Valor : %.1f" % (cadastro_valor[chave]))
                print(f"-------------------------\n")
    
    
    def buscar_fabricante(val):
                    
        for chave, value in cadastro_nome_fab_peca.items():

            if val == value:

                print(f"-------------------------\n")
                print(f"Código : {cadastro_codigo[chave]:03d}")
                print(f"Nome   : {chave}")                   
                print(f"Fabricante : {cadastro_nome_fab_peca[chave]}")                    
                print("Valor : %.1f" % (cadastro_valor[chave]))
                print(f"-------------------------\n")


    def remover_item(val):
                    
        for chave, value in cadastro_codigo.items():

            if val == value:
            
                cadastro_codigo.pop(chave)                  
                cadastro_nome_fab_peca.pop(chave)                    
                cadastro_valor.pop(chave)
          
            principal.consultarPeca()
            
    

    def menu():
    

        while True:

            try:


                print("""
Escolha a opção desejada:

1  - Cadastrar Peças
2  - Consultar Peças
3  - Remover Peças
4  - Sair""")

                opcao = int(input())
    
                if opcao == 1:
                
                    print("Você Selecionou a opção de cadastrar peça")

                    # Procura ultimo indice da lista
                    cont_indice =  len(contador) -1
                    cont_f = contador[cont_indice]

                    # Cria novo codigo       
                    cont = cont_f + 1 
                    contador.append(cont)
                        
                    principal.cadastrarPeca(cont)
            

                if opcao == 2:

                    principal.consultarPeca()
            
                if opcao == 3:

                    principal.removerPeca()

                if opcao == 4:
                
                    break 
            
                                    
            except(UnboundLocalError, ValueError):

                print(
                    """Você digitou uma opção invalida\nPor favor entre com a opção desejada novamente\n""")


    def cadastrarPeca(cont):

                print(f"Código da Peça: {cont:03d}")
        
                nome = str(input("Por Favor entre com o NOME da peça:"))
                fabricante = str(input("Por Favor entre com o FABRICANTE da peça:"))
                valor = int(input("Por Favor entre com o VALOR(R$) da peça:"))
        
                # Cadastro de codigo da peca, fabricante e valor
                cadastro_codigo[nome] = cont
                cadastro_nome_fab_peca[nome] = fabricante 
                cadastro_valor[nome] = valor
        

    def consultarPeca():
        
        while True:

            try:

                print("""
Você Selecionou a Opção de Consultar Peças
Escolha a opção desejada:
1   - Consultar Todas as Peças
2   - Consulta Peças por Código
3   - Consulta Peças por Fabricante
4   - Retornar""")

                consulta = int(input())

                if consulta == 1:

                    
                    for cad in cadastro_codigo and cadastro_nome_fab_peca and cadastro_valor:

                
                        print(f"-------------------------\n")
                        print(f"Código : {cadastro_codigo[cad]:03d}") 
                        print(f"Nome : {cad}")                  
                        print(f"Fabricante: {cadastro_nome_fab_peca[cad]}")                    
                        print("Valor : %.1f" % (cadastro_valor[cad]))
                        print(f"-------------------------\n")

            
                elif consulta == 2:

                        entrada_codigo = int(input("Digite o CÓDIGO da Peça:"))
                    
                        print(principal.buscar_codigo(entrada_codigo))

            
                elif consulta == 3:

                        entrada_codigo = input("Digite o FABRICANTE da Peça:")
                    
                        print(principal.buscar_fabricante(entrada_codigo))
                
                elif consulta == 4:

                    principal.menu()

            except(UnboundLocalError, ValueError):

                print(
                    """Você digitou uma opção invalida\nPor favor entre com a opção desejada novamente\n""")

    def removerPeca():

    
        while True:


                print("""
Você Selecionou a Opção de Remover Peça
""")

                entrada_remove = int(input("Digite o codigo da peça a ser removida:"))
                    
                
                print(principal.remover_item(entrada_remove))

         


id_pessoal()
principal.menu()

