import numpy as nl
import matplotlib.pyplot as plt
def plotar(tempos, tipo):
    plt.plot([100,1000,10000], tempos)
    plt.grid(True)
    plt.title(tipo)
    plt.xlabel("Quantidade de Nomes")
    plt.ylabel("Tempo em Milisegundos")
    plt.show()