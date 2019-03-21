def shellSort(vetor): #shell
    def shellsort(vetor):
        sublista = len(vetor)//2
        while sublista > 0:
            for inicio in range(sublista):
                insercao(vetor, inicio, sublista)
            
            sublista = sublista//2
    def insercao(vetor, inicio, ins):
        for i in range(inicio + ins, len(vetor), ins):
            valorAtual = vetor[i]
            posicao =  i

            while posicao >= ins and vetor[posicao - ins] > valorAtual:
                vetor[posicao] = vetor[posicao - ins]
                posicao = posicao - ins
            
            vetor[posicao] = valorAtual
    shellsort(vetor)
def mergeSort(vetor):
    if len(vetor)>1:
        metade = len(vetor)//2
        esquerda = vetor[:metade]
        direita = vetor[metade:]
        
        mergeSort(esquerda)
        mergeSort(direita)

        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k]=esquerda[i]
                i = i + 1
            else:
                vetor[k] = direita[j]
                j = j + 1
            k = k + 1

        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i = i + 1
            k = k + 1

        while j < len(direita):
            vetor[k] = direita[j]
            j = j + 1
            k = k + 1
def quickSort(vetor):#quick
    def quicksort(vetor):
        auxQuickSort(vetor,0,len(vetor)-1)
    
    def auxQuickSort(vetor, primeiro, ultimo):
        if primeiro < ultimo:
            dividirPonto = particao(vetor, primeiro, ultimo)

            auxQuickSort(vetor, primeiro,dividirPonto - 1)
            auxQuickSort(vetor, dividirPonto + 1, ultimo)
    
    def particao(vetor, primeiro, ultimo):
        pivo = vetor[primeiro]

        marcaEsquerda = primeiro + 1
        marcaDireita = ultimo

        Fim = False
        while not Fim:

            while marcaEsquerda <= marcaDireita and vetor[marcaEsquerda] <= pivo:
                marcaEsquerda = marcaEsquerda + 1
            
            while vetor[marcaDireita] >= pivo and marcaDireita >= marcaEsquerda:
                marcaDireita = marcaDireita - 1 
            
            if marcaDireita < marcaEsquerda:
                Fim = True
            else:
                temp = vetor[marcaEsquerda]
                vetor[marcaEsquerda] = vetor[marcaDireita]
                vetor[marcaDireita] = temp
    
        temp = vetor[primeiro]
        vetor[primeiro] = vetor[marcaDireita]
        vetor[marcaDireita] = temp

        return marcaDireita
    return quicksort(vetor)

