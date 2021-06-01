import ahkab
from ahkab import circuit, printing, time_functions
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

cont = 1
n = 3
r = np.array([0.1, 0.1, 0.01])
rajuste = np.zeros(n)
gain = np.zeros(2)


# Função Gaussiana responsável por fazer a aproximação do valor inserido pelo o usuário ao valor ideal
def v_random_float(n,cont):
    """
    [summary]

    Args:
        n ([int]): [description]
        cont ([int]): [description]

    Returns:
        [float]: [description]
    """
    return np.random.normal(np.zeros(n),0.99999**cont)


def simula_circuito(resistor1, resistor2, capacitor1):
    """
    [summary]

    Args:
        resistor1 ([float]): [description]
        resistor2 ([float]): [description]
        capacitor1 ([float]): [description]

    Returns:
        [float]: [description]
    """
    mycir = ahkab.Circuit('Filtro Passa-Baixa')

    voltage_step = time_functions.sin(vo=0, va=10, freq= 1000, td=0, theta=0, phi=0) 
    
    mycir.add_vsource("V1", "n1", mycir.gnd, dc_value=0, ac_value=10, function=voltage_step)
    mycir.add_resistor('R1', 'n1', 'n2', value = resistor1)
    mycir.add_capacitor('C1', 'n2', mycir.gnd, value = capacitor1)
    mycir.add_resistor('R2', 'n2', mycir.gnd, value = resistor2)

    freq_corte = 1 / (2 * math.pi * float(resistor1 * capacitor1))

    ac_analysis1000 = ahkab.new_ac(start=1000, stop=1000, points=1, x0=None, outfile='saida1000Hz')
    ac_analysis0 = ahkab.new_ac(start=0.01, stop=0.01, points=1, x0=None, outfile='saida0Hz')  
    
    r1000 = ahkab.run(mycir, ac_analysis1000)['ac']
    r0 = ahkab.run(mycir, ac_analysis0)['ac']
    
    resultado1000 = r1000.asarray()
    resultado0 = r0.asarray()
    
    gain[0] = 20*np.log10((np.abs(resultado1000[2])/np.abs(resultado1000[1])))
    gain[1] = 20*np.log10((np.abs(resultado0[2])/np.abs(resultado0[1])))

    return gain


def funcao_custo(resistor1, resistor2, capacitor1):
    ganho = simula_circuito(resistor1, resistor2, capacitor1)
    
    return (((ganho[0] + 6)**2) + ((ganho[1] + 3)**2))
    

y = funcao_custo(r[0], r[1], r[2])
melhory = y

while(melhory > 10):
    rmodificado = r + v_random_float(n, cont)
    y = funcao_custo(rmodificado[0], rmodificado[1], rmodificado[2])
    
    if y < melhory:
        melhory = y
        r = rmodificado 
    
    print(melhory)

print("R1:", np.absolute(r[0]),"Ω R1:", np.absolute(r[1]),"Ω C1:",np.absolute(r[2]),"F")