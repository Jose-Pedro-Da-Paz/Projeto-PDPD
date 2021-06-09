import random

a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))

x = 0
x2 = 0
xmelhor = 0

cont = 0

y = a * (x ** 2) + b * x + c
y2 = 0
ymelhor = a * (xmelhor ** 2) + b * x + c

if b == c == 0:
    print('Valor de y = 0 para x = 0')

while ymelhor != 0:
    
    x2 = random.random() -0.5
    x = xmelhor + x2
    
    if cont > 1000:
        x = xmelhor + (x2 / 10)

    y = a * (x ** 2) + b * x + c


    if ymelhor > y:
        xmelhor = x
        ymelhor = a * (xmelhor ** 2) + b * x + c
    
    cont += 1
    
    if cont == 100000:
        print('Não consegui achar o valor, a resolução é um Nº Complexo')
        break
    
    print('O melhor valor de y = {} para x = {}, {}ºtentativa'.format(ymelhor, xmelhor, cont))
    print('O valor atual de y = {} para x = {}'.format(y, x, ))

print('FIM!')
