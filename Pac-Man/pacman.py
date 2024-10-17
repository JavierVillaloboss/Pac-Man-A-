import random
from astar import a_star
from mapa import mapa

class PacMan:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.recolectadas = 0
        self.direccion = [1, 0]

    def mover(self):
        target = self.encontrar_pildora_cercana()
        if target:
            path = a_star(mapa, tuple(self.pos), target)
            if path and len(path) > 1:
                siguiente_pos = path[1]
                dx = siguiente_pos[0] - self.pos[0]
                dy = siguiente_pos[1] - self.pos[1]
                self.pos = siguiente_pos
                self.direccion = [dx, dy]
                if mapa[self.pos[1]][self.pos[0]] == 2:  # Consumir píldora
                    self.recolectadas += 1
                    mapa[self.pos[1]][self.pos[0]] = 0
        else:
            # Movimiento aleatorio si no encuentra píldoras cercanas
            self.mover_aleatorio()

    def encontrar_pildora_cercana(self):
        # Buscar píldora en un radio de 7x7
        for dy in range(-3, 4):
            for dx in range(-3, 4):
                nx, ny = self.pos[0] + dx, self.pos[1] + dy
                if 0 <= nx < len(mapa[0]) and 0 <= ny < len(mapa):
                    if mapa[ny][nx] == 2:
                        return (nx, ny)
        return None

    def mover_aleatorio(self):
        # Moverse aleatoriamente por los espacios vacíos
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Derecha, Izquierda, Abajo, Arriba
        random.shuffle(direcciones)  # Mezclar direcciones para movimiento aleatorio
        for dx, dy in direcciones:
            nueva_pos = [self.pos[0] + dx, self.pos[1] + dy]
            if 0 <= nueva_pos[0] < len(mapa[0]) and 0 <= nueva_pos[1] < len(mapa) and mapa[nueva_pos[1]][nueva_pos[0]] != 1:
                self.pos = nueva_pos
                self.direccion = [dx, dy]
                break
