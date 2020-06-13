# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:11:59 2019

@author: Josue
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:21:11 2019

@author: Josue
"""

#

import turtle as tur
import math
import numpy as np


#--- Calculo de la cinematica
def cinematica (theta,Vi,X,sampl,g):
    #Componente vectorial en Y
    Viy= Vi*(math.sin(math.radians(theta)))
    #Componente vectorial en X
    Vx= Vi*(math.cos(math.radians(theta)))
        
    #----Se calcula el tiempo total de la simulacion
    tT= X/Vx    
    #Creo mi vector de tiempo para muestrear en diferentes puntos la simulacion (N muestras)
    t=np.arange(tT/sampl,tT+(tT/sampl),tT/sampl)    
    #Calculo los desplazamientos en X
    deltaX= Vx * t     
    #Calculo los desplazamientos en Y
    deltaY= (Viy*t) + ((0.5*g)*(t*t))     
    return t, deltaX, deltaY 

#----------Se comprueba si llega a cero la pelota
def midePique(X,sampl,deltaX,deltaY):

    for i in range(0, len(deltaY)):
        if deltaY[i] <= 0:
            pique= i
            dist_falt=X- deltaX[pique]                        #Distancia faltante
            samp_falt= sampl - (pique+1)                          #muestras faltantes
            pique+= 1                                       #para que 
            break
        else:
            pique= len(deltaY)-1
            dist_falt=X- deltaX[pique]                        #Distancia faltante
            samp_falt= sampl - (pique+1)                          #muestras faltantes
            pique+= 1

    return pique, dist_falt, samp_falt

def pintaEscenario():
    tur.setup(600, 600, 0, 0)
    tur.screensize(300, 150)
    tur.title("Simulador tiro parabolico")
    tur.hideturtle()
    tur.colormode(255)
    
    tur.pensize(3)
    tur.pencolor(0,255,0)
    
    #Cesped
    tur.penup()
    tur.goto(-250, 0)
    tur.pendown()
    tur.goto(220, 0)
    
    
    tur.pensize(5)
    tur.pencolor(0,0,0)
    
    #Porteria
    tur.penup()
    tur.goto(220, 0)
    tur.pendown()
    tur.goto(220, 40)
    tur.goto(200,40)
    tur.goto(200,0)
    
    #Balon
    tur.penup()
    tur.goto(-250,0)
    tur.dot(10,0, 0, 0)




pintaEscenario()
#---------------------------------------
#-----------Parametros Cinematica
#---------------------------------------
#Angulo de disparo en grados
theta= 60                               #20
#Velocidad inicial en m/s
Vi= 5                             #15
#Distancia porteria-pelota en mts
X= 11                                   #22
#muestras de la simulacion
sampl= 50
#gravedad
g= -9.8
#factor amortiguamiento
D= 0.2

#Se calcula la trayectoria de la pelota
t, deltaX, deltaY= cinematica(theta,Vi,X,sampl,g)
# se calcula la distancia a la porteria de pique de la pelota
pique,dist_falt,samp_falt= midePique(X,sampl,deltaX,deltaY) 

Vi2=Vi
dist_falt2= dist_falt
samp_falt2=samp_falt
sumaPiques= pique


while(samp_falt2>0):
    Vi2= Vi2*(1-D) 
    t2, deltaX2, deltaY2= cinematica (theta,Vi2,dist_falt2,samp_falt2,g)
    
    pique2,dist_falt2,samp_falt2= midePique(deltaX2[len(deltaX2)-1],len(deltaX2),deltaX2,deltaY2) 

    
    #Se llena el vector con el rebote
    for i in range(0, (pique2)):
        deltaY[sumaPiques+i]=deltaY2[i]
    
    sumaPiques = sumaPiques+ pique2
    samp_falt2= sampl -sumaPiques
    dist_falt2=deltaX[0]*samp_falt2
        
#---------------------------------------
#---------------------------------------
#---------------------------------------
#dibujar trayectoria
tur.pendown()


disTot = 450   #distancia total entre balon y porteria en pixeles
posIni = -250  #inicia en la posicion -250

#Se escala en funcion de pixeles a metros
for i in range(0, len(t)):
    ajusteX= int((deltaX[i] * disTot)/X) + posIni      
    ajusteY= int((deltaY[i] * disTot)/X)
    
    if ajusteY >= -3:         #para pintar solo los positivos
        tur.pencolor(0,0,0)
        tur.goto(ajusteX,ajusteY)
        tur.dot(10,0, 0, 0)
    #else:
        #tur.pencolor(255,255,255)               #pinto de blanco
        #tur.goto(ajusteX,ajusteY)
        #tur.dot(10,0,0,0)
        
    
tur.done()



    
    
    