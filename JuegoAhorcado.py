# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:38:12 2022

@author: DiegoC
"""

# --- Es necesario primero cargar la base de datos con las palabras que se incluiran en el juego ---


import numpy as np

facil = np.array(['palabra1', 'palabra2', 'palabra3', 'palabra4', 'palabra5'])
medio = np.array(['palabra1', 'palabra2', 'palabra3', 'palabra4', 'palabra5'])
dificil = np.array(['palabra1', 'palabra2', 'palabra3', 'palabra4', 'palabra5'])

#---Definimos las funciones a utilizar

#---La función hang se encarga de "dibujar" al ahorcado dependiendo de los errores
def hang(wrans):
    if wrans == 0:
        print('------,')
        print('|')
        print('|')
        print('|')
    elif wrans == 1:
        print('------,')
        print('|     O')
        print('|')
        print('|')
    elif wrans == 2:
        print('------,')
        print('|     O')
        print('|    /|')
        print('|')
    elif wrans == 3:
        print('------,')
        print('|     O')
        print('|    /|\  ')
        print('|')
    elif wrans == 4:
        print('------,')
        print('|     O')
        print('|    /|\  ')
        print('|    /¯')
    elif wrans == 5:
        print('------,')
        print('|     O')
        print('|    /|\  ')
        print('|    /¯\  ')
    elif wrans == 6:
        print('♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫')
        print('       ☺/')
        print('      /|  ')
        print('      /¯\  ')
        print('♪♫♪♫♪♫♪♫♪♫♪♫♪♫♪♫')
    elif wrans == 7:
        print('')
        print('     ¯(xx)')
        print('      /|\ ')
        print('      /¯\  ')

#--- La función rsolv revisa si la letra ingresada se encuentra en la palabra
# y sustituye los _ de la palabra
def rsolv(lett, word, ul):
    rep = word.count(lett)
    if(rep > 0):
        for j in range(0,len(word)):
            if word[j] == lett:
                ul = ul[0:j]+ ul[j:].replace(ul[j], lett,1)
            else:
                ul = ul
    else:
        print(f'La letra {lett} no aparece en la palabra')
        
    return ul

#---Separa los '_' para que sea más facil la visualización
def wsp(txto):
    ntext = ''
    for k in range(0, len(txto)):
        ntext = ntext + txto[k] + ' '
    
    print(ntext)
#---El usuario selecciona el nivel 
pagain = 0

while pagain < 1:
    c = 0
    print('Seleccione el nivel que desea jugar: Facil(0), Medio(1), Dificil(2)')
    while c == 0:

        level = int(input())
        if (0<=level<=2):
            print(f'Ha seleccionado el nivel {level}')
            c=1
        else:
            print('el nivel seleccionado debe ser 0, 1 o 2')
            c = 0

#---Se selecciona una palabra al azar de la base de datos

    if level == 0:
        df = facil 
    elif level ==1:
        df = medio
    elif level == 2:
        df = dificil
        
    pmax=len(df)
    wrow = np.random.randint(0,pmax)
    gw = df[wrow]



    wa = 0 
    ul1 = ''
    for i in range(0,len(gw)):
        ul1 = ul1 + '_' 
    
    lused = ''
    
#---Inicia el juego el usuario tiene 5 intentos para adivinar
    hang(wa)
    
    wsp(ul1)
    while wa <= 5:
        if wa < 5:
            gg = input('Respuesta: ')
            repl = lused.count(gg)
            if len(gg) ==1:
                if repl ==0:
                    lused = lused + gg
                    ul =ul1
                    ul1 = rsolv(gg, gw, ul)
                    if ul1 == ul:
                        wa = wa+1
                    elif ul1 == gw:
                        print('¡Felicidades! Ganaste el juego')
                        wa = 6
                    hang(wa)
                    wsp(ul1)
                    slused = sorted(lused)
                    print(f'letras usadas: {slused}')
                    print('---------------------')
                else:
                    print('Ya se utilizo esa letra')
            else:
                print('Solo una letra por intento')
        elif wa==5:
            print(f'PERDISTE :( La palabra era: {gw}')
            wa = 7
            hang(wa)
    
    pagainp = 0
    while pagainp == 0:
        pagain = int(input('¿Desea jugar de nuevo? Sí(0) No(1):  '))
        if pagain == 0 or pagain ==1:
            pagainp = 1
        else:
            print('Debe seleccionar 0 para jugar de nuevo o 1 para salir del juego')
            