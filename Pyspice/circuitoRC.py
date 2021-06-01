import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Plot.BodeDiagram import bode_diagram
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

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

def simula_circuito(resistor1, capacitor1):
    '''

    '''
    circuit = Circuit('Filtro Passa Baixa RC')

    circuit.SinusoidalVoltageSource('input', '1', circuit.gnd, amplitude=10@u_V)
    R1 = circuit.R(1, '1', 'out', resistor1@u_kΩ)
    C1 = circuit.C(1, 'out', circuit.gnd, capacitor1@u_uF)

    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.ac(start_frequency=1@u_kHz, stop_frequency=1@u_kHz, number_of_points=1,  variation='dec')

    freq_corte = 1 / (2 * math.pi * float(R1.resistance * C1.capacitance))
    output = np.absolute(analysis.out)
    gain = 20*np.log10(output[0].value)

    '''for node in analysis.nodes.values():
        print('Node {}: {:5.2f} V'.format(str(node), float(node))) # Fixme: format value + '''

    
    return gain

def funcao_custo(resistor1, capacitor1):
    ganho = simula_circuito(resistor1, capacitor1)
    return ((ganho + 10 )**2)
    

y = funcao_custo(r[0],r[1])
melhory = y

while(melhory > 0.0001):
    rmodificado = r + v_random_float(n,cont)
    y = funcao_custo(rmodificado[0], rmodificado[1])
    if y < melhory:
        melhory = y
        r = rmodificado 
    print(melhory)
print("R1:", np.absolute(r[0]),"kΩ  C1:",np.absolute(r[1]),"uF")

