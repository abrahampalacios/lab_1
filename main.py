
# coding: utf-8

# Abrahan Palacios 
# 22347628
# USE EL JUPYTER PARA REALIZAR ESTE LABORATORIO.
#NO LO PROBE EN PYTHON SOLAMENTE, LO PASE DEL FORMATO DE JUPYTER A .PY
# In[4]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas
import matplotlib.pyplot as plt 
import pylab

# Importamos el archivo student-por.csv
filename = 'student-por.csv'

data = pandas.read_csv(filename, delimiter=";")
data['studytime'].plot(kind="hist")
pylab.show()


# In[124]:

#4
plt.xlabel('Cantidad de faltas')
plt.ylabel('Tiempo libre')
plt.scatter(data['absences'],data['traveltime'])
#plt.show()
#Se puede observar que la cantidad de faltas va en relación al tiempo de viaje debido a que las 
#estudiantes que viven lejos son los que menos faltan.


# In[16]:

#Mostrar elementos sobre los datos


#numero de elementos del dataframe
print(data.size)

#Promedio de notas del G1
print(np.mean(data.G1))

#Maximo numero de faltas
print (np.max(data.absences))

#Minima edad de los estudiantes
print (np.min(data.age))

#numero de fallos 
print (np.sum(data.failures))

#Varianza de las edades de los estudiantes
print (np.var(data.age))



# In[145]:

# ALGORITMOS
#Determinar el promedio de falta de  estudiantes dependiendo del estado civil de sus padres.
a= data[ (data.Pstatus=='A')]
a= np.mean(a.absences)
b=data[ (data.Pstatus!='A')]
b= np.mean(b.absences)
print a
print b


# In[162]:

# Promedio de tiempo de estudio por estudiantes de distintos generos
a= data[ (data.sex =='F')]
a= np.mean(a.studytime)
b=data[ (data.sex=='M')]
b= np.mean(b.studytime)
print a
print b


# In[172]:

# Promedio de tiempo de estudio por estudiantes de distintos generos
a= data[ (data.higher =='yes')]
avga=(a.G3+a.G2+a.G1)/3
a= np.mean(avga)
b=data[ (data.higher =='no')]
avgb=(b.G3+b.G2+b.G1)/3
b= np.mean(avgb)
print a
print b


# In[ ]:



