import random
import time
import datetime

def reiniciar_tablero(lista):
  for i in range(filas_matriz):
    for j in range(columnas_matriz):
      lista[i][j] = ' '

lista =[]
filas_matriz = int(input('Ingrese la cantidad de filas del tablero'))
columnas_matriz = int(input('Ingrese la cantidad de columnas del tablero'))
for i in range(filas_matriz):
  lista.append([])
  for j in range(columnas_matriz):
    lista[i].append(' ')
for item in lista:
  print(item)
cantidad_muros = int(input('Ingrese la cantidad de muros que desea ingresar'))
while True:
  for _ in range(cantidad_muros):
    col = random.randint(0, columnas_matriz -1)
    fila = random.randint(0, filas_matriz- 1)
    if lista[fila][col] == ' ':
      lista[fila][col] = '#'

  col = random.randint(0,2)
  #print(col)
  fila = random.randint(0,3)
  #print(fila)
  
  
  
  lista[fila][col] = 'M'
#lista.append([1])
  
  #imprime el tablero
  for item in lista:
    print(item)
  time.sleep(3)
  hora = datetime.datetime.now()
  print('Esta es la hora:', hora)
  print('='*columnas_matriz)
  reiniciar_tablero(lista)
#print(lista)
