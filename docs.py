import numpy as np
import math

docs = ["El procesamiento de lenguaje natural permite a las computadoras comprender textos",
		"Machine learning utiliza datos y algoritmos para entender patrones",
		"El procesamiento de lenguaje natural y modelos de machine learning analizan textos y datos"]

stop_words = {'el', 'de', 'a', 'las', '.', 'y', 'para'}
res,vocabulario = [], []

for i in range (len(docs)):
	docs[i] = docs[i].lower().split()


for i in range(len(docs)):
	res.append([p for p in docs[i] if p not in stop_words])
resa = [p for f in res for p in f]

for p in resa:
	if p not in vocabulario:
		vocabulario.append(p)

total = [[0 for _ in range(len(vocabulario))]for _ in range(len(res))]

for i in range(len(docs)):
	for j in range(len(vocabulario)):
		if vocabulario[j] in res[i]:
			total[i][j] += 1

#solo sirve para mostrar mas bonito las palabras y el num de veces que aparece por documento
rotado = np.array(total)
rotado = rotado.T

#sumamos los valores de las columnas xd
frecuencia = (np.sum(total,axis = 0)).tolist()

print("Las veces que se repiten las palabras por cada documento son: \n")

print(f"{"Palabra":<15} \t Doc(1,2,3) \t Total")
for j in range(len(vocabulario)):		
	print(f"{vocabulario[j]:<15}: \t {rotado[j]} \t = {frecuencia[j]}")
probabilidad, idf = [], []

for i in range (len(frecuencia)):
	probabilidad.append(frecuencia [i] / len(frecuencia))
	idf.append(math.log(3/frecuencia[i],10))

print("\n\n\t\t\t probabilidad  \t  IDF ")

for i in range(len(probabilidad)):
	print(f"{vocabulario[i]:<15}: \t  {probabilidad[i]:.4f} \t {idf[i]:.4f}" )

