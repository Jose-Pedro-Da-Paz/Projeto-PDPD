# Importa as bibliotecas utilizadas no código 
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import csv

# Declaração das funções que estão sendo utilizadas no código 

# Função responsável por armazenar a função matematica que sera calculada 
def funcao(x, n):
    y = (((x[0]**2)+x[1]-11)**2)+((x[0]+(x[1]**2)-7)**2)
    return y

# Função Gaussiana responsável por fazer a aproximação do valor inserido pelo o usuário ao valor ideal
def v_random_float(n,cont):
    return np.random.normal(np.zeros(n),0.99999**cont)



numero = 10.0*(10**(-16))


# Início do código: Define os valores iniciais, e a quantidade de vezes que o código vai ser executado 
for i in range(0,1):

    n = 2

    x = np.zeros(n)
    xajuste = np.zeros(n)

    for i in range(0,n):
        x[i] = (random.randint(-25,25) - random.random())


    xmelhor = x
    ymelhor = funcao(xmelhor,n)


    cont = 0
# Parte do código onde ocorre a aproximação ao valor desejado, a partir do Algoritmo Hill Climbing 
    while ymelhor >= numero:
      
        x = xmelhor + v_random_float(n,cont)

        y = funcao(x,n)

        if ymelhor > y:
            xmelhor = x
            ymelhor = y

    
      

   
        cont += 1
        
        print(' y = {:.4f}, {:.4f} tentativa'.format(ymelhor,cont))
        
        if ymelhor <= numero:
            print('FIM DE UM CICLO!')
            break

    #plt.show()
# Armazena os dados em um DataFrame para ser analisados 


    #pegar data e  hora para guardar no arquivo
    from datetime import datetime
    data_e_hora_atuais = datetime.now()
    #data_e_hora_em_texto = data_e_hora_atuais.strftime(‘%d/%m/%Y’)
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

    #gravar os dados ------------------------------------------------------
    arquivo = open("jpedro01.txt", "a")    # abre o arquivo para gravar no final
    arquivo.write("Execucao em "+data_e_hora_em_texto+";")   # grava data e hora no arquivo
    #gravando valores de x
    for i in range(0,n):  
        arquivo.write(str(x[i])+";")  # precisa converter para string para gravar
        # gravar os valores finais de x, y e contador 
    arquivo.write(str(ymelhor) + ";" + str(xmelhor) + ";" + str(cont))   # grava ymelhor, xmelhor, cont
    arquivo.write("\n")   # grava uma quebra-de-linha no arquivo
    arquivo.close()  # fechar o arquivo    
    
