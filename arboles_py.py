class par():
    def __init__(self, letra, frecuencia):
        self.letra = letra
        self.frecuencia = frecuencia
    
def texto():
    import os
    os.chdir("/media/cristiandavid/CURSOS FEC/UNSA 2022 CC/semestre par/CC/discretas_2/Arboles/")
    # creando un archivo que lea los string de un documento
    text = open('text.txt')
    valor =  text.readline().replace('\n','').lower()
    blinded = ''
    while valor != '':
        blinded += valor
        valor = text.readline().replace('\n','').lower()
    return blinded
def frecuencia(letra, texto):
    contador = 0
    for i in texto:
        if letra == i:
            contador += 1
    return contador
def mayor(iterable):
    posicion = 0
    mayor = iterable[0]
    for i in iterable:
        if i > mayor:
            mayor = i
    for posicion in range(len(iterable)):
        if iterable[posicion] == mayor:
            break
    return mayor, posicion
#%%
def ordenamiento(iterable):
    ordenado = []
    copia = iterable.copy()
    while len(ordenado) != len(iterable):
        number, pos = mayor(copia)
        ordenado.append(copia[pos])
        del copia[pos]    
                
    return ordenado         
    


#%%
texto = texto()
contador = 0
unicos = []
for i in texto:
        if i not in unicos:
            unicos.append(i)
# ahora creare la estrucutra que contenga tanto la cantidad de letras como sus 
# frecuencias
estructuras = []
for i in unicos:
    par_i = par(i, frecuencia(i,texto))
    estructuras.append(par_i)

estructuras[2].frecuencia
type(estructuras[1])

mayor(estructuras.frecuencia)


#%%
a = [1,56,89,25]
var = a[3]
a[3] = a[2]
a[2] = var
print(a)
#%%
var = a[2]
a[2] = a[1]
a[1] = var

#%%
import numpy as np
import scipy as sp
a =np.random.randint(0,100,5)
print(a)
# a = [155555454545454,56,89,25,125,452,2,568,1235,1235512,12,123,12,41,25,125,12,5,1254,124]
mayor = a[0]
contador = 0
for j in range(len(a)-1,-1,-1):
    for i in range(j+1):
        if a[i] >= mayor :
            mayor = a[i]
            pos = contador
        contador += 1
    var = a[j]
    a[j] = a[pos]
    a[pos] = var     
    print(j, pos)
    contador = 0
    mayor = 0
print (a)


#%%

# hallando las letras unicas y colocarlas en un vector


a = 'wallecio por un impacto ni nada por el estilo, tenemos d opciones convo'

unicos = []
unicos.append(a[0])
unicos
repeticiones = 0
for i in a:
    for j in range(len(unicos)):
        if i == unicos[j]:
            repeticiones += 1
    if repeticiones == 0:
        unicos.append(i)
    repeticiones = 0
    
unicos























































































