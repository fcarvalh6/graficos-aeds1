import matplotlib.pyplot as plt

#esse programa gera três gráficos, um para cada tipo de vetor usado para a ordenação (crescente, decrescente e aleatório)
#insira as coordenadas entre os colchetes da seguinte forma: a,b,c,d ...

#VETOR CRESCENTE

#BubbleSort
xcb = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
ycb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do BubbleSort no vetor crescente
plt.plot(xcb, ycb, label = "BubbleSort")

#SelectionSort
xcs = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
ycs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do SelectionSort no vetor crescente
plt.plot(xcs, ycs, label = "SelectionSort")

#InsertionSort
xci = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
yci = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do InsertionSort no vetor crescente
plt.plot(xci, yci, label = "InsertionSort")

#Decorando o gráfico
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Número de Operações')
plt.title('Vetor Crescente')

plt.legend()
plt.show()

#VETOR ALEATÓRIO

#BubbleSort
xab = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
yab = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do BubbleSort no vetor aleatório
plt.plot(xab, yab, label = "BubbleSort")

#SelectionSort
xas = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
yas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do SelectionSort no vetor aleatório
plt.plot(xas, yas, label = "SelectionSort")

#InsertionSort
xai = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
yai = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do InsertionSort no vetor aleatório
plt.plot(xai, yai, label = "InsertionSort")

#Decorando o gráfico
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Número de Operações')
plt.title('Vetor Aleatório')

plt.legend()
plt.show()

#VETOR DECRESCENTE

#BubbleSort
xdb = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
ydb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do BubbleSort no vetor decrescente
plt.plot(xdb, ydb, label = "BubbleSort")

#SelectionSort
xds = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
yds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do SelectionSort no vetor decrescente
plt.plot(xds, yds, label = "SelectionSort")

#InsertionSort
xdi = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
ydi = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

#Gráfico do InsertionSort no vetor decrescente
plt.plot(xdi, ydi, label = "InsertionSort")

#Decorando o gráfico
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Número de Operações')
plt.title('Vetor Decrescente')

plt.legend()
plt.show()