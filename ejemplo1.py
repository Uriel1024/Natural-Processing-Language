import numpy as np
import math
doc1 = "El procesamiento de lenguaje natural permite a las computadoras comprender textos"
doc2 = "Machine learning utiliza datos y algoritmos para entender patrones"
doc3 = "El procesamiento de lenguaje natural y modelos de machine learning analizan textos y datos"
stop_words = {'el', 'de', 'a', 'las', '.', 'y', 'para'}


doc1 = doc1.lower().split()
doc2 = doc2.lower().split()
doc3 = doc3.lower().split()

res1 = [p for p in doc1 if p not in stop_words]
res2 = [p for p in doc2 if p not in stop_words]
res3 = [p for p in doc3 if p not in stop_words]
rest = res1 + res2 + res3
vocabulario = []
for p in rest:
	if p not in vocabulario:
		vocabulario.append(p)


rest = [res1,res2,res3]
#para guardar el total de res
total = [[0 for _ in range (len(vocabulario))]for _ in range(3)]

for i in range(3):
	for j in range(len(vocabulario)):
		if vocabulario[j] in rest[i]:
			total[i][j] += 1

print("Las veces que se repiten las palabras por cada documento son:")
print(vocabulario)
for j in range(3):		
	print(f"Doc{j}: {total[j]} ")


#sumamos los valores de las columnas xd
frecuencia = (np.sum(total,axis = 0)).tolist()
print("Las veces que se repiten las palabras en total es:")
for i in range(len(frecuencia)):
	print(f"{vocabulario[i]}: {frecuencia[i]}")

probabilidad,idf = [],[]

for i in range (len(frecuencia)):
	probabilidad.append(frecuencia [i] / len(frecuencia))
	idf.append(math.log(3/frecuencia[i],10))

print("La probabilidad y el IDF es:")

for i in range(len(probabilidad)):
	print(f"{vocabulario[i]}: \t  {probabilidad[i]:.4f} \t {idf[i]:.4f}" )

