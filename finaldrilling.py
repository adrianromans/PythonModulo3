lista_nombres = ['Harry Houdini', 'David Blaine', 'Teller', 'Newton', 'Hawking', 'Einstein', 'Gandhi', 'Shakespeare', 'Mozart']

magos = []
cientificos = [] 
otros = []

"""y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase El gran antes del nombre de cada mago. """

def hacer_grandioso():
    global magos
    magos = ['El gran ' + nombre for nombre in magos]


def imprimir_nombres():
    print('Magos: ', magos)
    print('Cientificos: ', cientificos)
    print('Otros: ', otros)

"""Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros;"""

for nombre in lista_nombres: 
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

"""Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes."""

print('Lista de nombres completa:')
imprimir_nombres()
print('---------------')

print('Lista con Magos grandiosos:')
hacer_grandioso()
imprimir_nombres()

