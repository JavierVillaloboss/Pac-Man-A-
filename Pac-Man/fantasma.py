import random
from astar import a_star
from mapa import mapa

class Fantasma:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.posiciones_anteriores = []  # Lista para rastrear las posiciones anteriores

    def mover(self, pacman_pos):
        # Intentar encontrar a Pac-Man
        if self.detectar_pacman(pacman_pos):
            path = a_star(mapa, tuple(self.pos), tuple(pacman_pos))
            if path and len(path) > 1:
                siguiente_pos = path[1]
                self.pos = siguiente_pos
        else:
            # Movimiento aleatorio si no detecta a Pac-Man
            self.mover_aleatorio()

        # Comprobar si está atascado en la misma posición
        self.comprobar_atasco()

    def detectar_pacman(self, pacman_pos):
        # Detectar a Pac-Man en un radio de 7x7
        return abs(pacman_pos[0] - self.pos[0]) <= 3 and abs(pacman_pos[1] - self.pos[1]) <= 3

    def mover_aleatorio(self):
        # Moverse aleatoriamente por los espacios vacíos
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(direcciones)  # Mezclar direcciones para movimiento aleatorio
        for dx, dy in direcciones:
            nueva_pos = [self.pos[0] + dx, self.pos[1] + dy]
            if 0 <= nueva_pos[0] < len(mapa[0]) and 0 <= nueva_pos[1] < len(mapa) and mapa[nueva_pos[1]][nueva_pos[0]] != 1:
                self.pos = nueva_pos
                break

    def comprobar_atasco(self):
        # Agregar la posición actual a las posiciones anteriores
        self.posiciones_anteriores.append(tuple(self.pos))

        # Si ha estado en la misma posición durante más de 3 ciclos, cambiar de dirección
        if len(self.posiciones_anteriores) > 3 and all(pos == self.pos for pos in self.posiciones_anteriores[-3:]):
            self.mover_aleatorio()  # Forzar un movimiento aleatorio si está atascado

        # Limitar la longitud de la lista de posiciones anteriores
        if len(self.posiciones_anteriores) > 10:
            self.posiciones_anteriores.pop(0)
