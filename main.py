import numpy as np
import matplotlib.pyplot as plt


def make_array(*data:list)->'list[np.ndarray]':
    array = []
    for d in data:
        array.append(np.array(d))

    return array

def integrate(data:np.ndarray)->np.ndarray:
    retour = []
    temp = 0
    for e in data:
        temp+=e
        retour.append(temp)
    return np.array(retour)

print("Initialisation des données")

R = 1 #résistance du circuit
C = 0.10 #capacité du condensateur
Q_init = 0 #charge initial du condensateur en Coulomb
E_target = 5 #tension visée en Volt 


tf = 10*R*C #environ

h = 0.001
U_f = E_target*0.95 #tension de fon de boucle




I = [0]
Q = [0]
U_c = [0]
U_r = [0]
U_g = [0]



T = [0]

def fE(t:float)->float:
    """Tension d'alimentation"""
    #return E_target #tension continue constante
    #return E_target* (t/tf) #tension linéaire
    return E_target*np.log(t+1) #tension logarithmique
def fU_r(i:float)->float:
    """Tension de la résistance en fonction de l'intensité"""
    return R*i

def fU_c(q:float):
    """Tension du condensateur en fonction de la charge"""
    return q/C 

print("Lancement de la simulation...")
while U_c[-1]<U_f:
    t = T[-1]+ h
    
    q = Q[-1] + I[-1] * h
    e = fE(t)
    u_c = fU_c(q)
    u_r = e - u_c
    i = u_r/R

    T.append(t)
    Q.append(q)
    U_c.append(u_c)
    U_r.append(u_r)
    U_g.append(e)
    I.append(i)


print("Génération des graphiques")    

I ,Q ,U_c,U_r ,U_g ,T = make_array(I,Q,U_c,U_r,U_g,T)

P_r = U_r * I
P_c = U_c * I
P_g = U_g * I

E_r = integrate(P_r)
E_c = integrate(P_c)
E_g = integrate(P_g)

fig = plt.figure()
#graphique affichant les tensions du circuit
U_ax = fig.add_subplot(2,2,1)
U_ax.plot(T,U_g,label="Ug")
U_ax.plot(T,U_r,label="Ur")
U_ax.plot(T,U_c,label="Uc")
U_ax.set_title("Tension")
U_ax.set_ylabel("Tension en Volt")
U_ax.set_xlabel("Temps en s")
U_ax.legend()


I_ax = fig.add_subplot(2,2,2)
I_ax.plot(T,I,label="I")
I_ax.set_ylabel("Intensité en A")
I_ax.set_xlabel("Temps en s")
I_ax.set_title("Intensité")
I_ax.legend()

E_ax = fig.add_subplot(2,2,3)
E_ax.plot(T,E_c,label="Ec")
E_ax.plot(T,E_r,label="Er")
E_ax.plot(T,E_g,label="E")
E_ax.set_ylabel("Energie en J")
E_ax.set_xlabel("Temps en s")
E_ax.set_title("Energie")
E_ax.legend()

P_ax = fig.add_subplot(2,2,4)
P_ax.plot(T,P_c,label="Pc")
P_ax.plot(T,P_r,label="Pr")
P_ax.plot(T,P_g,label="P")
P_ax.set_ylabel("Puissance en W")
P_ax.set_xlabel("Temps en s")
P_ax.set_title("Puissance")
P_ax.legend()

E_end = E_c[-1]
E_lost = E_r[-1]
E_total = E_g[-1]

rendement = E_end/E_total
print(f"Rendement : {rendement}")
print(f"Temps : {T[-1]}")
plt.show()