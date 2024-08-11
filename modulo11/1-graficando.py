import matplotlib.pyplot as mpl # Importamos la librería de gráficos de matplotlib para generar gráficos y le asignamos un alias mpl

def generate_bar_chart(labels, values): # Definimos una función que recibe dos listas, labels y values
    
    fig, ax = mpl.subplots() # Creamos una figura y un eje para el gráfico con la función subplots de mpl
    ax.bar(labels, values) # Creamos un gráfico de barras con la función bar de mpl y le pasamos las listas labels y values
    mpl.show() # Mostramos el gráfico con la función show de mpl
    
    
def generate_pie_chart(labels, values):
    
    fig, ax = mpl.subplots()
    ax.pie(values, labels=labels) # Creamos un gráfico de pastel con la función pie de mpl y le pasamos las listas labels y values
    ax.axis('equal') # Hacemos que el gráfico sea un círculo perfecto
    mpl.show()
    
if __name__ == '__main__': # Si el script se ejecuta directamente, ejecutamos el siguiente código
    labels = ['A', 'B', 'C', 'D']
    values = [1, 4, 2, 5]
    generate_pie_chart(labels, values)