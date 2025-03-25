import numpy as np
import matplotlib.pyplot as plt

R = 1 #résistance du circuit
C = 0.10 #capacité du condensateur
Q_init = 0 #charge initial du condensateur en Coulomb
E_target = 5 #tension visée en Volt 


h = 0.1
N = 10*R*C/h

def E(t:float)->float:
    """Tension d'alimentation"""
    return E_target

I = []
U_c = []
U_r = []
U_g = [E(0)]
T = []


for n in range(N):
    pass
