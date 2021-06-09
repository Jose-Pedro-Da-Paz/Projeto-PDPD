# Importa as bibliotecas necessárias
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math


# define função teste
def f(x):
    x1 = x[0]
    x2 = x[1]
    fx = (((x1**2)+x2-11)**2)+((x1+(x2**2)-7)**2)
    return fx

# Ponto de inicio --> Determina  o ponto de partida da procura
x_start = [4, 4]

# gráfico ou algo assim kkkk
i1 = np.arange(-5.0, 5.0, 0.01)
i2 = np.arange(-5.0, 5.0, 0.01)
x1m, x2m = np.meshgrid(i1, i2)
fm = (((x1m**2)+x2m-11)**2)+((x1m+(x2m**2)-7)**2) #Função a ser otimizada

# Geração da figura onde vai ser armazenada os dados para o gráfico
plt.figure()

# Specify contour lines 
#lines = range(2,52,2)

# Plot contours
CS = plt.contour(x1m, x2m, fm, 50)#,lines)

# Label contours
plt.clabel(CS, inline=1, fontsize=10)

# Add some text to the plot
plt.title('Non-Convex Function')
plt.xlabel('x1')
plt.ylabel('x2')


##################################################
# Simulated Annealing
##################################################

# Número de Cíclos
n = 50

# Número de tentativas por ciclo
m = 50

# Número de soluções aceitas
na = 0.0

# Probabilidade de ser aceito uma solução pior no começo do algoritmo
p1 = 0.7

# Probabilidade de ser aceito uma solução pior no final do algoritmo
p50 = 0.001

# "Temperatura inicial"
t1 = -1.0/math.log(p1)

# "Temperatura final"
t50 = -1.0/math.log(p50)

# redução fracionada que ocorre por ciclo
frac = (t50/t1)**(1.0/(n-1.0))

# Inicia x
x = np.zeros((n+1,2))
x[0] = x_start
xi = np.zeros(2)
xi = x_start
na = na + 1.0

# melhor resultado para x
xc = np.zeros(2)
xc = x[0]
fc = f(xi)
fs = np.zeros(n+1)
fs[0] = fc

# temperatura atual
t = t1
pior = 0

# DeltaE médio
DeltaE_avg = 0.0
for i in range(n):
    print('Cycle: ' + str(i) + ' with Temperature: ' + str(t))

    for j in range(m):
        # gera novos pontos para ser testados
        xi[0] = xc[0] + random.random() - 0.5
        xi[1] = xc[1] + random.random() - 0.5
        # limita mázimos e minimos onde serão procurados as respostas
        xi[0] = max(min(xi[0],5.0),-5.0)
        xi[1] = max(min(xi[1],5.0),-5.0)
        DeltaE = abs(f(xi)-fc)

        if (f(xi)>fc):
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
            xc[0] = xi[0]
            xc[1] = xi[1]
            fc = f(xc)
            
            # incrementa o número de soluções aceitas
            na = na + 1.0
            
            # Atualiza DeltaE_avg
            DeltaE_avg = (DeltaE_avg * (na-1.0) +  DeltaE) / na
    
    # Guarda os melhores valores de x no fim de cada ciclo
    x[i+1][0] = xc[0]
    x[i+1][1] = xc[1]
    fs[i+1] = fc
    
    # diminui a "temperatura" para o próximo ciclo
    t = frac * t

# printa as soluções
print('Best solution: ' + str(xc))
print('Best objective: ' + str(fc))
print(pior)
print(x)

plt.plot(x[:,0],x[:,1],'y-o')
plt.savefig('contour.png')

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(fs,'r.-')
ax1.legend(['Objective'])

ax2 = fig.add_subplot(212)
ax2.plot(x[:,0],'b.-')
ax2.plot(x[:,1],'g--')
ax2.legend(['x1','x2'])

# salva a figura como um png
plt.savefig('iterations.png')

plt.show()
