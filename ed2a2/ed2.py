from sorts import *
import timeit
from graficos import plotar

from tkinter import messagebox
#messagebox, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel
def imprimir(vetor):
    x = 0
    num_elementos_lista = len(vetor)
    while(x < num_elementos_lista):
        print(vetor[x])
        x += 1
datadir = './data/'
print('Análise de tempode de execução de Algoritimos')

print('1 - Shell')
print('2 - Merge')
print('3 - Quick')
idSort = input('Qual algoritimo deseja executar:  ');

arq = open(datadir+"nomes10000.txt", 'r', 9, 'utf-8')

words = arq.readlines()

for i in range(len(words)):  # tratar as palavras
    words[i] = words[i].rstrip('\n')
arq.close()

tempos = []
cem = words[:100]
mil = words[:1000]
Dmil = words[:10000]

if int(idSort) == 1:
    tipo = "ShellSort"
    for i in range(3):
        inicio = timeit.default_timer()
        if i == 0:
            shellSort(cem)
        elif i == 1:
            shellSort(mil)
        else:
            shellSort(Dmil)
        fim = timeit.default_timer()
        tempos.append(fim - inicio)
    plotar(tempos, tipo)

elif int(idSort) == 2:
    tipo = "MergeSort"
    for i in range(3):
        inicio = timeit.default_timer()
        if i == 0:
            mergeSort(cem)
        elif i == 1:
            mergeSort(mil)
        else:
            mergeSort(Dmil)
        fim = timeit.default_timer()
        tempos.append(fim - inicio)
    plotar(tempos, tipo)
elif int(idSort) == 3:
    tipo = "QuickSort"
    for i in range(3):
        inicio = timeit.default_timer()
        if i == 0:
            quickSort(cem)
        elif i == 1:
            quickSort(mil)
        else:
            quickSort(Dmil)
        fim = timeit.default_timer()
        tempos.append(fim - inicio)
    plotar(tempos, tipo)
else:
    print('Comando inválido.')

messagebox.showinfo(tipo, cem)