import ahkab
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

cont = 1
n = 2
r = np.random.rand(n)
rajuste = np.zeros(n)

# Função Gaussiana responsável por fazer a aproximação do valor inserido pelo o usuário ao valor ideal
def v_random_float(n,cont):
    return np.random.normal(np.zeros(n),0.99**cont)


def simula_circuito(resistor1, resistor2): 
    mycir = ahkab.Circuit('Divisor de Tensão')

    mycir.add_vsource('V1', 'n1', mycir.gnd, dc_value=10)
    mycir.add_resistor('R1', 'n1', 'n2', value = resistor1)
    mycir.add_resistor('R2', 'n2', mycir.gnd, value = resistor2)


    opa = ahkab.new_op(outfile='teste')
    r = ahkab.run(mycir, opa)['op']
    resultado = r.asarray()
    
    return resultado[1]

def funcao_custo(resistor1, resistor2):
    tensao = simula_circuito(resistor1, resistor2)
    return ((tensao - 5)**2)
    

y = funcao_custo(r[0],r[1])
melhory = y

while(melhory > 0.000001):
    rmodificado = r + v_random_float(n,cont)
    y = funcao_custo(rmodificado[0], rmodificado[1])
    if y < melhory:
        melhory = y
        r = rmodificado
    print(melhory)
print(r)