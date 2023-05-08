import numpy as np
import variables as var
from clases import *
import funciones
from os import system

class HLF():

    def __init__(self, num_jugadores=var._num_jugadores):
 
        self.num_jugadores = num_jugadores
        self.jugadores = {}
        
        self.bienvenida()
        self.set_jugadores()
        for i in range(self.num_jugadores):
            self.jugadores[f'jugador_{i}'] = Jugador()
        self.nueva_partida()
        

    def bienvenida(self):
        system('cls')
        print('¡BIENVENIDO A HUNDIR LA FLOTA!')

    def set_jugadores(self):
        while self.num_jugadores < 0 or self.num_jugadores > 2:
            self.num_jugadores = int(input('Introduce el número de jugadores: '))

    def nueva_partida(self):
        while (_vidas):
            pass
    
HLF()