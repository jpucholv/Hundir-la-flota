import numpy as np
import variables as var
import random


class Jugador():

    def __init__(self, nombre=var._nombre, barcos=var._barcos, disparos=var._disparos):
        self.nombre = self.set_nombre() # self.set_nombre(), nombre
        self.barcos = self.barcos_random() # self.barcos_random(), barcos
        self.disparos = disparos
        self.tablero = Tablero(self.barcos)

    def set_nombre(self):
        self.nombre = input('Introduce tu nombre: ')
        return self.nombre

    def set_barcos(self):
        pass

    def barcos_random(self, eslora1=4, eslora2=3, eslora3=2, eslora4=1):
        barcos = []

        for i in range(eslora1):
            barcos.append(Barco(eslora=1).get_barco())
        for i in range(eslora2):
            barcos.append(Barco(eslora=2).get_barco())
        for i in range(eslora3):
            barcos.append(Barco(eslora=3).get_barco())
        for i in range(eslora4):
            barcos.append(Barco(eslora=4).get_barco())
        
        self.barcos = barcos

    def disparar(self, disparo=var._disparo):
        self.disparo = disparo
        
        while x < 0 or x > 9:
            x = [int(input('Introduce la coordenada X de tu disparo: '))]
        while y < 0 or y > 9:
            y = int(input('Introduce la coordenada Y de tu disparo'))
        
        self.disparo = np.array([x,y])
        self.disparos.concatenate(self.disparo)
        return self.disparo


class Tablero():

    def __init__(self, tablero=var._tablero, barcos=var._barcos):
        self.barcos = barcos
        self.visto = tablero.copy()
        self.set_visto()
        self.oculto = tablero.copy()


    def set_visto(self):
        visto = self.visto.copy()
        for barco in self.barcos:
            bandera = True
            for i in range(barco['eslora']):
                x = barco['pos_inicial'] + (i * var._dict_orientaciones[barco['orientacion']])
                if visto[x] == ' ':
                    visto[x] = 'O'
                else:
                    bandera = False
            
            if bandera:
                self.visto = visto
            else:
                print(f'{barco} no pudo ser colocado.')

    def actualizar_oculto(self, disparo, enemigos):
        if enemigos[disparo[0], disparo[1]] == 'O':
            self.oculto[disparo[0], disparo[1]] = 'X'
        else:
            self.oculto[disparo[0], self.oculto[1]] = '-'

    def actualizar_visto(self, disparo, ):
        if self.visto[disparo[0], disparo[1]] == 'O':
            self.visto[disparo[0], disparo[1]] = 'X'
        else:
            self.visto[disparo[0], self.visto[1]] = '-'


class Barco():
    
    def __init__(self, pos_inicial= np.random.randint(0, 10, (1,2)),
                 eslora=random.randint(1, 5),
                 orientacion=random.choice(('N', 'S', 'E', 'O'))):
        
        self.barco = {'pos_inicial': pos_inicial,
                      'eslora': eslora,
                      'orientacion': orientacion}
        
    def set_barco(self):
        self.barco['poscicion_inicial'] = np.array(input(f'Introduce la posición inicial de {self.barco}: '))
        self.barco['eslora'] = int(input(f'Introduce la eslora de {self.barco}: '))
        self.barco['orientacion'] = input(f'Introduce la orientación de {self.barco}: ').upper()

    def get_barco(self):
        return self.barco