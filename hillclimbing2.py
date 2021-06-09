import random
import numpy as np
import matplotlib as plt

x1 = random.randint(0,100)
x2 = random.randint(0,100)
x3 = random.randint(0,100)

xmelhor1 = random.randint(0,100)
xmelhor2 = random.randint(0,100)
xmelhor3 = random.randint(0,100)

x = np.array([x1, x2, x3])

y0 = x**2
y = y0[0]+y0[1]+y0[2]

xmelhor = np.array([xmelhor1, xmelhor2, xmelhor3])
ymelhor = xmelhor[0]**2 + xmelhor[1]**2 + xmelhor[2]**2

cont = 0

def v_random():
    for i in range(0,3):   
        x[i] = random.randint(0,100)


while ymelhor != 0:
     v_random()
     y0 = x**2
     y = y0[0]+y0[1]+y0[2]

     if ymelhor > y:
          for j in range(0,3):
               xmelhor[j] = x[j]

          ymelhor = xmelhor[0]**2 + xmelhor[1]**2 + xmelhor[2]**2

     cont += 1

     if cont == 300000:
         print('Não consegui achar o valor, a resolução é um Nº Complexo')
         break

     print('O melhor valor de y = {} para x = {}, {}ºtentativa'.format(ymelhor,xmelhor,cont))
     print('O valor atual de y = {} para x = {}'.format(y,x))

print('FIM!') 
