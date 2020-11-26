import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
cont = 0
grafico = []

x1 = float(input("Digite um valor inicial para x: "))
x2 = float(input("Digite um valor inicial para y: "))
x = np.array([x1, x2])
xajuste = np.array([x1, x2])
xmelhor1 = x1
xmelhor2 = x2
xmelhor = np.array([xmelhor1, xmelhor2])
ymelhor = ((xmelhor[0] + (2*xmelhor[1]) + 7)**2 + ((2*xmelhor[0]) + xmelhor[1] - 5)**2)



def v_random_float():
    for i in range(0,2):   
        xajuste[i] = random.gauss(0,(0.99**cont))



y = ((x[0] + (2*x[1]) + 7)**2 + ((2*x[0]) + x[1] - 5)**2)

while ymelhor != 0:
    
    
    v_random_float() 
    
    for i in range(0,2):
        x[i] = xmelhor[i] + xajuste[i]



    if ymelhor > y:
        for j in range(0,2):
            xmelhor[j] = x[j]
        ymelhor = ((xmelhor[0] + (2*xmelhor[1]) + 7)**2 + ((2*xmelhor[0]) + xmelhor[1] - 5)**2)

    
    grafico.append(ymelhor)
    
    plt.plot(np.log(grafico), color='red')
   
    
    

    cont += 1
    if cont == 2000:
        print('Acabou as tentativas')
        break
    print('O melhor valor de y = {} para x = {}, {}ºtentativa'.format(ymelhor,xmelhor,cont))
    "print('O valor atual de y = {} para x = {}'.format(y,x))"
print('FIM!') 
plt.show()
