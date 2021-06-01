import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

import random
import numpy as np
from pprint import pprint

cont = 1
n = 2
r = np.random.rand(n)
rajuste = np.zeros(n)

# Função Gaussiana responsável por fazer a aproximação do valor inserido pelo o usuário ao valor ideal
def v_random_float(n,cont):
    '''
    
    '''
    return np.random.normal(np.zeros(n),0.99**cont)

def simula_circuito(resistor1, resistor2):
    circuit = Circuit('Voltage Divider')

    circuit.V('input', 1, circuit.gnd, 10@u_V)
    circuit.R(1, 1, 2, resistor1@u_kΩ)
    circuit.R(2, 2, circuit.gnd, resistor2@u_kΩ)

    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.operating_point()


    '''for node in analysis.nodes.values():
        print('Node {}: {:5.2f} V'.format(str(node), float(node))) # Fixme: format value + '''

    Tensao_no_2 = float(analysis['2'])
    return Tensao_no_2

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
print(np.abs(r))






