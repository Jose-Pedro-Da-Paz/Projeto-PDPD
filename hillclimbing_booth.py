import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def funcao(x, n):
    y = (((x[0] + (2*x[1]) - 7)**2) + (((2*x[0]) + x[1] - 5)**2))
    return y


def v_random_float(n,cont):
    for i in range(0,n):   
        xajuste[i] = random.gauss(0,(0.99**cont))
    return xajuste



n = 2

x = np.zeros(n)
xajuste = np.zeros(n)

for i in range(0,n):
    x[i] = float(input("Digite um suposto valor para x{}: ".format(i)))


xmelhor = x
ymelhor = funcao(xmelhor,n)

cont = 0
grafico = []



while ymelhor != 0:
      
    x = xmelhor + v_random_float(n,cont)

    y = funcao(x,n)

    if ymelhor > y:
        xmelhor = x
        ymelhor = y

    
    grafico.append(ymelhor)
    
    plt.plot(np.log(grafico), color='red')
   
    cont += 1
    if cont == 2000:
        print('Acabou as tentativas')
        break
    print('O melhor valor de y = {} para x = {}, {}ºtentativa'.format(ymelhor,xmelhor,cont))
    '''print('O valor atual de y = {} para x = {}'.format(y,x))'''
print('FIM!') 
plt.show()
