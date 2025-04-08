# Archivo: tres_valores.py
# Fecha: 08/04/2025
# Proy.: studio de algoritmos
#
# Ordenar crecientemente una lista de tres valores.
# Existe un error, ya que según los valores, puede cambiar
# dos que entre ellos había que cambiar, pero genera mal orden
# en los posteriores.

# Función swap(int indice)
n = []

# Bucle para tomar datos del teclado y guardarlos en la variable n de tipo lista
for in range(3):
    n.append(int(input())) #append es un método de las listas

    s = n # Voy a hacer dos intetos de ordenar. Para tener
          # la lista original sin cambio, tendré que copiarla a otra lista
          # y así trabajamos con la copia

    for i in range(2):    #Aquí se refleja el error p.ej. con [7, 5, 3]
        if s[i] > s[i+1]:
            a = s[i]
            s[i] = s[i+1]
            s[i+1] = a
print(s)

s = n
for i in range(len(n)-2):  #Aquí hacemos el repaso a la lista dos veces
    for j in range(len(n)-1):
        if s[j] > s[j+1]:
            a = s[j]
            s[j]