import matplotlib.pyplot as plt

#esse programa gera três gráficos, um para cada tipo de vetor usado para a ordenação (crescente, decrescente e aleatório)
#insira as coordenadas entre os colchetes da seguinte forma: a,b,c,d ...

#VETOR CRESCENTE

#BubbleSort
xcb = [1,2,3]
ycb = [1,2,3]

#Gráfico do BubbleSort no vetor crescente
plt.plot(xcb, ycb, label = "BubbleSort")

#SelectionSort
xcs = [1,2,3]
ycs = [1,2,3]

#Gráfico do SelectionSort no vetor crescente
plt.plot(xcs, ycs, label = "SelectionSort")

#InsertionSort
xci = [1,2,3]
yci = [1,2,3]

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
xab = [1,2,3]
yab = [1,2,3]

#Gráfico do BubbleSort no vetor aleatório
plt.plot(xab, yab, label = "BubbleSort")

#SelectionSort
xas = [1,2,3]
yas = [1,2,3]

#Gráfico do SelectionSort no vetor aleatório
plt.plot(xas, yas, label = "SelectionSort")

#InsertionSort
xai = [1,2,3]
yai = [1,2,3]

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
xdb = [1,2,3]
ydb = [1,2,3]

#Gráfico do BubbleSort no vetor decrescente
plt.plot(xdb, ydb, label = "BubbleSort")

#SelectionSort
xds = [1,2,3]
yds = [1,2,3]

#Gráfico do SelectionSort no vetor decrescente
plt.plot(xds, yds, label = "SelectionSort")

#InsertionSort
xdi = [1,2,3]
ydi = [1,2,3]

#Gráfico do InsertionSort no vetor decrescente
plt.plot(xdi, ydi, label = "InsertionSort")

#Decorando o gráfico
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Número de Operações')
plt.title('Vetor Decrescente')

plt.legend()
plt.show()