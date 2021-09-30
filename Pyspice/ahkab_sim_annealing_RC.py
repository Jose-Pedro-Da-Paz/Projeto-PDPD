import ahkab
from ahkab import circuit, printing, time_functions
import bokeh
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

num = 2 # Determina a quantidade de "espaços" que serão criados nos vetores
cont = 1 # contador
r = np.random.rand(num)
rajuste = np.zeros(num)
k = 0

# Simulated Annealing
n = 50 # Número de Cíclos
m = 75 # Número de tentativas por ciclo
na = 0.0 # Número de soluções aceitas
p1 = 0.7 # Probabilidade de ser aceito uma solução pior no começo do algoritmo
p50 = 0.001 # Probabilidade de ser aceito uma solução pior no final do algoritmo
t1 = -1.0/math.log(p1) # "Temperatura inicial"
t50 = -1.0/math.log(p50) # "Temperatura final"
frac = (t50/t1)**(1.0/(n-1.0)) # redução fracionada que ocorre por ciclo


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
        xinicio[k] = float(input("x{} ínicio: ".format(k)))
    return xinicio 


def simula_circuito(resistor1, capacitor1): 
    mycir = ahkab.Circuit('Filtro Passa-Baixa')

    voltage_step = time_functions.sin(vo=0, va=10, freq= 1000, td=0, theta=0, phi=0) 
    mycir.add_vsource("V1", "n1", mycir.gnd, dc_value=0, ac_value=10, function=voltage_step)
    mycir.add_resistor('R1', 'n1', 'n2', value = resistor1)
    mycir.add_capacitor('C1', 'n2', mycir.gnd, value = capacitor1)

    freq_corte = 1 / (2 * math.pi * float(resistor1 * capacitor1))
    ac_analysis = ahkab.new_ac(start=1000, stop=1000, points=1, x0=None, outfile='saida') 
    r = ahkab.run(mycir, ac_analysis)['ac']
    resultado = r.asarray()
    gain = 20*np.log10((np.abs(resultado[2])/np.abs(resultado[1])))
    
    return gain

def funcao_custo(resistor1, capacitor1):
    ganho = simula_circuito(resistor1, capacitor1)
    return ((ganho + 3 )**2)
    
    



# Inicia x
x = np.zeros((n+1,num))
x[0] = entrada_valor(num)
xi = np.zeros(num)
xi = x[0]
na = na + 1.0

# melhor resultado para x
xc = np.zeros(num)
xc = np.copy(x[0])
fc = funcao_custo(xi[0], xi[1])
fs = np.zeros(n+1)
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
            xi[k] = max(min(xi[k],5.0),-5.0)
        
        DeltaE = abs(funcao_custo(xi[0], xi[1])-fc)
        
        if (funcao_custo(xi[0], xi[1])>fc):
            # Inicializa DeltaE_avg se encontrar uma soluçao pior
            #   Na primeira iteração
            
            if (i==0 and j==0): DeltaE_avg = DeltaE
            # Função objetivo é pior
            # gera a probabilidade de aceitar ou não a solução pior
            p = math.exp(-DeltaE/(DeltaE_avg * t))
            # determina se aceita o pior ponto
            
            if (random.random()<p):
                # aceita a pior solução
                accept = True
                pior += 1
            else:
                # Não aceita a pior solução
                accept = False

        else:
            # se a função objetivo for menor automaticamente aceita
            accept = True
        
        if (accept==True):
            # Atualiza as novas soluções aceitas 
            
            for k in range(num):
                xc[k] = xi[k]
            fc = funcao_custo(xc[0], xc[1])
            # incrementa o número de soluções aceitas
            na = na + 1.0
            # Atualiza DeltaE_avg
            DeltaE_avg = (DeltaE_avg * (na-1.0) +  DeltaE) / na
    # Guarda os melhores valores de x no fim de cada ciclo
    
    for k in range(num):
        x[i+1][k] = xc[k]
    fs[i+1] = fc
    # diminui a "temperatura" para o próximo ciclo
    t = frac * t

# printa as soluções
print('Best solution: ' + str(xc))
print('Best objective: ' + str(fc))
