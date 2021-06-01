import ahkab
from ahkab import circuit, printing, time_functions
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd

cont = 1
n = 2
r = np.random.rand(n)
rajuste = np.zeros(n)
gain = np.zeros(2)

# Função Gaussiana responsável por fazer a aproximação do valor inserido pelo o usuário ao valor ideal
def v_random_float(n,cont):
    return np.random.normal(np.zeros(n),0.99**cont)


def simula_circuito(): 
    mycir = ahkab.Circuit('Filtro Amplificador')

    mycir.add_model('ekv', 'Suyama', {'TYPE':'n', 'VTO':1, 'KP':2e-3})

    voltage_step = time_functions.sin(vo=0, va=1, freq= 1000, td=0, theta=0, phi=0) 
    mycir.add_vsource("Vsig", "n1", mycir.gnd, dc_value=0, ac_value= 1, function=voltage_step)
    mycir.add_vsource("V1", "nV", mycir.gnd, dc_value=18)

    mycir.add_mos("M1", "nd","ng", "ns", "nb", w=1, l=1, model_label='Suyama')

    mycir.add_resistor('Rsig', 'n1', 'n2', value = (50*(10**3)))
    mycir.add_capacitor('C1', 'n2',"ng", value = 1)
    mycir.add_resistor('R1', 'ng', 'nV', value = (10*(10**6)))
    mycir.add_resistor('R3', 'ng', mycir.gnd, value = (10*(10**6)))
    
    mycir.add_resistor('R2', 'nd', 'nV', value = (8*(10**3)))
    mycir.add_capacitor('C2', 'nd',"nVo", value = 1)
    mycir.add_resistor('R5', 'nVo', mycir.gnd, value = (5*(10**3)))

    mycir.add_resistor('R4', 'ns', mycir.gnd, value = (3*(10**3)))
    mycir.add_capacitor('C3', 'ns',mycir.gnd, value = 1)
   
    tran_analysis = ahkab.new_tran(tstart=0, tstop=0.1,tstep=5e-6, x0=None, outfile='Transiente')
    r0 = ahkab.run(mycir, tran_analysis)['tran']
    print(r0.asarray())

     

sla = simula_circuito()
print(sla)

df = pd.read_csv("Transiente.tran")


