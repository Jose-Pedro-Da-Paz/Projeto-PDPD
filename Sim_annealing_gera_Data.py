import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import pandas as pd

k = 0
num = 2
cont = 0
df = pd.DataFrame(columns = ['X0' , 'F(x)', 'x', 'cont'])


# define função teste
def f(x):
    # fx = (((x[0] ** 2) + x[1] - 11) ** 2) + ((x[0] + (x[1] ** 2) - 7) ** 2) himmeblaus
    m = 10
    d = 2
    fx = 0

    for i in range(1, d+1):
        fx += (np.sin(x[i-1]) * ((np.sin((i*(x[i-1]**2)/(np.pi))))**(2*m)))
    
    fx = -fx
    return fx


# Ponto de inicio --> Determina  o ponto de partida da procura
def entrada_valor(num):
    """
    entrada_valor tem como função receber os valores que o usuário 
    insere. E armazena em um vetor xinicio, este vetor determina 
    qual será o ponto de início de procura do algoritmo pelo melhor valor 
    que soluciona a função custo.
    Args:
        num ([int]): número de váriaves da função custo
    Returns:
        [float]: Retorna o vetor que indica qual é o ponto de ínicio do algoritmo
    """
    xinicio = np.zeros(num)
    for k in range(num):
        xinicio[k] = random.randint(-5,5) + random.random()
    return xinicio 



while cont <= 1000:
    ##################################################
    # Simulated Annealing
    ##################################################

    # Número de Cíclos
    n = 100

    # Número de tentativas por ciclo
    m = 500

    # Número de soluções aceitas
    na = 0.0

    # Probabilidade de ser aceito uma solução pior no começo do algoritmo
    p1 = 0.5

    # Probabilidade de ser aceito uma solução pior no final do algoritmo
    p50 = 0.001

    # "Temperatura inicial"
    t1 = -1.0/math.log(p1)

    # "Temperatura final"
    t50 = -1.0/math.log(p50)

    # redução fracionada que ocorre por ciclo
    frac = (t50 / t1) ** (1.0 / (n - 1.0))

    # chama entrada_valor

    # Inicia x
    x = np.zeros((n + 1, num))

    x[0] = entrada_valor(num)
    xi = np.zeros(num)
    xi = np.copy(x[0])
    na = na + 1.0

    # melhor resultado para x
    xc = np.zeros(num)
    xc = np.copy(x[0])
    fc = f(xi)
    fs = np.zeros(n + 1)
    fs[0] = fc

    # temperatura atual
    t = t1
    pior = 0

    # DeltaE médio
    DeltaE_avg = 0.0

    for i in range(n):
        print('Ciclo: ' + str(i) + ' Temperatura: ' + str(t))
    
        for j in range(m):
            # gera novos pontos para ser testados
            for k in range(num):
                xi[k] = xc[k] + random.random() - 0.5
                # limita máximos e minimos onde serão procurados as respostas
                xi[k] = max(min(xi[k], 5.0), -5.0)
        
            DeltaE = abs(f(xi) - fc)
        
            if (f(xi) > fc):
                # Inicializa DeltaE_avg se encontrar uma soluçao pior
                #   Na primeira iteração
                if (i==0 and j==0): DeltaE_avg = DeltaE
            
                # Função objetivo é pior
                # gera a probabilidade de aceitar ou não a solução pior
                p = math.exp(-DeltaE / (DeltaE_avg * t))
            
                # determina se aceita o pior ponto
                if (random.random() < p):
                    # aceita a pior solução
                    accept = True
                    pior += 1
                else:
                    # Não aceita a pior solução
                    accept = False

            else:
                # se a função objetivo for menor automaticamente aceita
                accept = True
        
            if (accept == True):
                # Atualiza as novas soluções aceitas 
                for k in range(num):
                    xc[k] = xi[k]
                fc = f(xc)
            
                # incrementa o número de soluções aceitas
                na = na + 1.0
            
                # Atualiza DeltaE_avg
                DeltaE_avg = (DeltaE_avg * (na - 1.0) +  DeltaE) / na
    
        # Guarda os melhores valores de x no fim de cada ciclo
        for k in range(num):
            x[i + 1][k] = xc[k]
    
        fs[i + 1] = fc

    
        # diminui a "temperatura" para o próximo ciclo
        t = frac * t


    df.loc[cont] = [x[0], fc, xc, cont]


    cont += 1
print(df)
df.to_csv('michalewicz_n100_m500.csv ', sep='\t')
print("===========FINAL===============")   