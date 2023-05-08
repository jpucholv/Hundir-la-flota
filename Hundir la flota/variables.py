import numpy as np

_num_jugadores = -1 # 0 1 2
_dict_orientaciones = {'N': np.array([-1, 0]),
                       'S': np.array([1, 0]),
                       'E': np.array([0, 1]),
                       'O': np.array([0, -1])}
_nombre = 'ANY'
_barcos = [{'pos_inicial': np.array((0,1)), 'eslora': 2, 'orientacion':'S'},
           {'pos_inicial': np.array((1,3)), 'eslora':4, 'orinetacion':'E'}]
_tablero = np.full((10, 10), ' ')
_disparo = np.random.randint(0, 10, (1,2))
_disparos = []