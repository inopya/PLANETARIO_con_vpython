# -*- coding: cp1252 -*-

#         _\|/_
#         (O-O)               A ver, que tenemos por aqui....
# -----oOO-(_)-OOo----------------------------------------------------


#######################################################################
# ******************************************************************* #
# *                                                                 * #
# *                   Autor:  Eulogio López Cayuela                 * #
# *                                                                 * #
# *                 Planetario Educativo con vPython                * #
# *                                                                 * #
# *                  Versión 2.3   Fecha: 24/11/2015                * #
# *                                                                 * #
# ******************************************************************* #
#######################################################################



from __future__ import division

# Importar vPython para generar mundo virtual 
from visual import * 

# Importar librerias para crear controles
from visual.controls import *


#--------------------------------------------------------
# DEFINICION DE FUNCIONES
#--------------------------------------------------------

def mostarOrbitas(indice):
    '''
    # Funcion llamada por el click sobre el boton. Es la encargada de
    # mostrar u ocultar las estelas de las orbitas
    '''
    global cuerpos_celestes, tiempos_estela, lista_botones, etiquetas_botones
    colorOff=(0.68,0.68,0.68)
    if cuerpos_celestes[indice].retain!=0:
        cuerpos_celestes[indice].retain = 0
        lista_botones[indice].text = etiquetas_botones[indice]+' off'
        lista_botones[indice].button.color = colorOff
    else:
        cuerpos_celestes[indice].retain = tiempos_estela[indice]
        lista_botones[indice].text = etiquetas_botones[indice]+' on'
        lista_botones[indice].button.color = color.green




#-------------------------------------------------------- 
# CREAR LA VENTANA PARA LOS BOTONES DE CONTROL
#--------------------------------------------------------

ventanaControl = controls(title='Botones de control', x=800, y=00,
                          width=200, height=500)#, range=110)

# Crear botones para mostrar u ocultar trayectorias
anchoBoton = 45
altoBoton = 16
posX = -10
colorOn=color.green
b0 = button( pos=(posX,55), width=anchoBoton, height=altoBoton, color=colorOn,
              text='Mercurio on', action=lambda: mostarOrbitas(0) )
b1 = button( pos=(posX,45), width=anchoBoton, height=altoBoton, color=colorOn,
              text='Venus on', action=lambda: mostarOrbitas(1) )
b2 = button( pos=(posX,35), width=anchoBoton, height=altoBoton, color=colorOn,
              text='tierra on', action=lambda: mostarOrbitas(2) )
b3 = button( pos=(posX,25), width=anchoBoton, height=altoBoton, color=colorOn,
              text='luna on', action=lambda: mostarOrbitas(3) )
b4 = button( pos=(posX,15), width=anchoBoton, height=altoBoton, color=colorOn,
              text='Marte on', action=lambda: mostarOrbitas(4) )
b5 = button( pos=(posX,5), width=anchoBoton, height=altoBoton, color=colorOn,
              text='jupiter on', action=lambda: mostarOrbitas(5) )
b6 = button( pos=(posX,-5), width=anchoBoton, height=altoBoton, color=colorOn,
              text='saturno on', action=lambda: mostarOrbitas(6) )
b7 = button( pos=(posX,-15), width=anchoBoton, height=altoBoton, color=colorOn,
              text='urano on', action=lambda: mostarOrbitas(7) )
b8 = button( pos=(posX,-25), width=anchoBoton, height=altoBoton, color=colorOn,
              text='netpuno on', action=lambda: mostarOrbitas(8) )
b9 = button( pos=(posX,-35), width=anchoBoton, height=altoBoton, color=colorOn,
              text='pluton on', action=lambda: mostarOrbitas(9) )

lista_botones = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9]
etiquetas_botones = ['mercurio','venus','tierra','luna','marte','jupiter','saturno','urano','netpuno','pluton']
# Crear un boton para modificar la velocidad
s1 = slider( pos=(-30,80),length = 60, min = 20, max = 2600, height=1,
              text='Velocidad', value = 20 )

##t_marte = toggle(pos=(40,-30), width=10, height=10, text0='off', text1='Marte', action=lambda: togglecubecolor())
##t_marte.settoggle(1)

verOrbitas = True
didactica = True
#radio base
#r = 1

#Valores iniciales de las variables para almacenar las posiciones angulares
a1 = 0.0 #giro mercurio
a2 = 0.0 #giro venus
a3 = 0.0 #giro tierra
a4 = 0.0 #giro luna
a5 = 0.0 #giro marte
a6 = 0.0 #giro jupiter
a7 = 0.0 #giro saturno
a8 = 0.0 #giro urano
a9 = 0.0 #giro neptuno
a10 = 0.0 #giro pluton



#Relacion entre los periodos de translacion de los planetas
#velocidads en relacion a la velocidad terrestre
year = 365.0  # un año 365 dias

velocidad_Virtual = 0.006 #velocidad vpython 0.006
v_mercurio = year/88
v_venus = year/224.5
v_tierra = 1
v_marte = year/(year+321)
v_jupiter = year/(11*year+315)
v_saturno = year/(29*year+167)
v_urano = year/(84*year+7)
v_neptuno = year/(164*year+280)
v_pluton = year/(247*year+249)



#Distancias al sol (en millones de kilometros)
AjusteDistancia = 58.0
ds_mercurio = 58.0 / AjusteDistancia
ds_venus = 108.0 / AjusteDistancia
ds_tierra = 150.0 / AjusteDistancia
ds_tierraLuna = 155.0 / AjusteDistancia  #dato inventado. buscarlo
ds_marte = 228.0 / AjusteDistancia
ds_jupiter = 778.0 / AjusteDistancia
ds_saturno = 1429.0 / AjusteDistancia
ds_urano = 2870.0 / AjusteDistancia
ds_neptuno = 4501.0 / AjusteDistancia
ds_pluton = 5900.0 / AjusteDistancia

#Diametros los distintos cuerpos del sistema solar (en miles de kilometros)
#(para dividir el diametro al menos entre 2 para obtener el radio)
ajuste_radio = 2.0 * 350.00 #para conseguir una escala real de los objetos y que quepan en pantalla
'''
r_sol = 1390.0 / ajuste_radio
r_mercurio = 4.878 / ajuste_radio
r_venus = 12.1 / ajuste_radio
r_tierra = 12.756 / ajuste_radio
r_marte = 6.786 / ajuste_radio
r_jupiter = 142.2 / ajuste_radio
r_saturno = 120.536 / ajuste_radio
r_urano = 51.118 / ajuste_radio
r_neptuno = 49.528 / ajuste_radio
r_pluton = 2.4 / ajuste_radio
'''
r_sol = 1390.0 / ajuste_radio
r_mercurio = 4.9 / ajuste_radio
r_venus = 12.1 / ajuste_radio
r_tierra = 12.8 / ajuste_radio
r_marte = 6.8 / ajuste_radio
r_jupiter = 142.2 / ajuste_radio
r_saturno = 120.5 / ajuste_radio
r_urano = 51.1 / ajuste_radio
r_neptuno = 49.5 / ajuste_radio
r_pluton = 2.4 / ajuste_radio

#tiempo_estela = [mercurio,venus,tierra,luna,marte,jupiter,saturno,urano,netpuno,pluton]
tiempo_estela = [40,40,80,190,190,400,395,400,400,390]

if didactica==True:
    #Distancias al sol, falseadas para que visualmente resulte didactico
    ds_mercurio = 3
    ds_venus = 4
    ds_tierra = 8
    ds_tierraLuna = 0.95
    ds_marte = 13
    ds_jupiter = 18
    ds_saturno = 24
    ds_urano = 31
    ds_neptuno = 34
    ds_pluton = 36


    #radios, falseados para que los objetos resulten visualmente 'didacticos'
    r_sol = 2
    r_mercurio = 0.15
    r_venus = 0.2
    r_tierra = 0.6
    r_marte = 0.4
    r_jupiter = 1.1
    r_saturno = 1.0
    r_urano = 0.5
    r_neptuno = 0.45
    r_pluton = 0.13

#--------------------------------------------------------
# DIBUJAR OBJETOS 3D EN LA ESCENA
#--------------------------------------------------------

#creamos un sol
sol = sphere(radius=r_sol, pos=(0, 0, 0),
            color=color.yellow, material=materials.emissive)
luzSolar = local_light(pos=sol.pos, color=sol.color)

#creamos un plano que corta el centro del sistema planetario (para mejorar la visualizacion
#boxy = box(size=(50, 50, 0.00001), color=(0.5, 0.5, 0.5), material=materials.rough)

mercurio = sphere(radius=r_mercurio, pos=(ds_mercurio, 0, 0), make_trail=verOrbitas, interval=6, retain=40,
            color=color.orange, material=materials.plastic)

venus = sphere(radius=r_venus, pos=(ds_venus, 0, 0), make_trail=verOrbitas, interval=15, retain=40,
            color=color.green, material=materials.plastic)

tierra = sphere(radius=r_tierra, pos=(ds_tierra, 0, 0), make_trail=verOrbitas, interval=12, retain=80,
            color=color.blue, material=materials.plastic)

luna = sphere(radius=0.15, pos=(ds_tierra+ds_tierraLuna, 0, 0), make_trail=verOrbitas, interval=5, retain=190,
            color=color.white, material=materials.plastic)

marte = sphere(radius=r_marte, pos=(ds_marte, 0, 0), make_trail=verOrbitas, interval=10, retain=190,
            color=color.red, material=materials.plastic)


jupiter = sphere(radius=r_jupiter, pos=(ds_jupiter, 0, 0), make_trail=verOrbitas, interval=30, retain=400,
            color=color.orange, material=materials.plastic)

saturno = sphere(radius=r_saturno, pos=(ds_saturno, 0, 0), make_trail=verOrbitas, interval=75, retain=395,
            color=color.white, material=materials.plastic)

anilloForma = shapes.circle(radius=2*r_saturno, thickness=0.7)
# extrusion de los anillos para darle cuerpo
anillos = extrusion(pos=[(0,0,-0.035),(0,0,0.035)], shape=anilloForma, color=color.white,
            make_trail=verOrbitas, interval=40, retain=400, material=materials.plastic)

urano = sphere(radius=r_urano, pos=(ds_urano, 0, 0), make_trail=verOrbitas, interval=210, retain=400,
            color=color.white, material=materials.plastic)

neptuno = sphere(radius=r_neptuno, pos=(ds_neptuno, 0, 0), make_trail=verOrbitas, interval=405, retain=400,
            color=color.green, material=materials.plastic)


pluton = sphere(radius=r_pluton, pos=(ds_pluton, 0, 0), make_trail=verOrbitas, interval=660, retain=390,
            color=color.green, material=materials.plastic)


cuerpos_celestes = [mercurio,venus,tierra,luna,marte,jupiter,saturno,urano,neptuno,pluton]
tiempos_estela = [40,40,80,190,190,400,395,400,400,390]

#-------------------------------------------------------- 
# BUCLE DEL PROGRAMA PARA ATENDER EVENTOS
#-------------------------------------------------------- 
FPS = 20
while True:
    rate(s1.value)
    mercurio.pos = ds_mercurio*vector(cos(a1), sin(a1), mercurio.z)
    a1 += velocidad_Virtual*v_mercurio

    venus.pos = ds_venus*vector(cos(a2), sin(a2), venus.z )
    a2 += velocidad_Virtual*v_venus

    tierra.pos = ds_tierra*vector(cos(a3), sin(a3), tierra.z)
    luna.pos = ds_tierra*vector(cos(a3), sin(a3), tierra.z) + ds_tierraLuna*vector(cos(a4), sin(a4), tierra.z) 
    a3 += velocidad_Virtual
    a4 += 0.078 #0.078 genera 13 vueltas, realmente da 13,5

    marte.pos = ds_marte*vector(cos(a5), sin(a5), marte.z )
    a5 += velocidad_Virtual*v_marte

    jupiter.pos = ds_jupiter*vector(cos(a6), sin(a6), jupiter.z )
    a6 += velocidad_Virtual*v_jupiter

    saturno.pos = ds_saturno*vector(cos(a7), sin(a7), saturno.z)
    anillos.pos = ds_saturno*vector(cos(a7), sin(a7), saturno.z)
    a7 += velocidad_Virtual * v_saturno    

    urano.pos = ds_urano*vector(cos(a8), sin(a8), urano.z )
    a8 += velocidad_Virtual*v_urano

    neptuno.pos = ds_neptuno*vector(cos(a9), sin(a9), neptuno.z )
    a9 += velocidad_Virtual*v_neptuno

    pluton.pos = ds_pluton*vector(cos(a10), sin(a10), pluton.z )
    a10 += velocidad_Virtual*v_pluton



