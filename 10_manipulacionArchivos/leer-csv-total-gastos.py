'''
Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60
'''

import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      total = 0
      for row in reader:
        print(row)
        total += int(row[1])
      return total
  
print('input: data.csv\n')
response = read_csv('modulo10/data.csv')

print('Output:\n',response)
