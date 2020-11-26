import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



x1 = float(input("Digite um suposto valor para x1: "))
x2 = float(input("Digite um suposto valor para x2: "))
x3 = float(input("Digite um suposto valor para x3: "))

xmelhor1 = x1
xmelhor2 = x2
xmelhor3 = x3

x = np.array([x1, x2, x3])
xajuste = np.array([x1, x2, x3])
y0 = x**2
y = y0[0]+y0[1]+y0[2]
xmelhor = np.array([xmelhor1, xmelhor2, xmelhor3])

ymelhor = xmelhor[0]**2 + xmelhor[1]**2 + xmelhor[2]**2

cont = 0
grafico = []


def v_random_float():
    for i in range(0,3):   
        xajuste[i] = random.gauss(0,(0.99**cont))

while ymelhor != 0:
    
    
    v_random_float() 
    
    for i in range(0,3):
        x[i] = xmelhor[i] + xajuste[i]

    y0 = x**2
    y = y0[0]+y0[1]+y0[2]

    if ymelhor > y:
        for j in range(0,3):
            xmelhor[j] = x[j]
        ymelhor = xmelhor[0]**2 + xmelhor[1]**2 + xmelhor[2]**2

    
    grafico.append(ymelhor)
    
    plt.plot(np.log(grafico), color='red')
   
    
    

    cont += 1
    if cont == 2000:
        print('Não consegui achar o valor, a resolução é um Nº Complexo')
        break
    print('O melhor valor de y = {} para x = {}, {}ºtentativa'.format(ymelhor,xmelhor,cont))
    print('O valor atual de y = {} para x = {}'.format(y,x))
print('FIM!') 
plt.show()
