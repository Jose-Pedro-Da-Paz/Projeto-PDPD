import ahkab
from ahkab import circuit, printing, time_functions
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


def simula_circuito(resistor1, resistor2, capacitor1): 
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
    

y = funcao_custo(r[0],r[1])
melhory = y

while(melhory > 0.01):
    rmodificado = r + v_random_float(n,cont)
    y = funcao_custo(rmodificado[0], rmodificado[1])
    if y < melhory:
        melhory = y
        r = rmodificado 
    print(melhory)
print("R1:", np.absolute(r[0]),"Ω  C1:",np.absolute(r[1]),"F")