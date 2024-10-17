import pygame
from constantes import ANCHO, ALTO, AZUL, TAM_CELDA
from mapa import dibujar_mapa, mapa
from pacman import PacMan
from fantasma import Fantasma

# Inicializar Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man")  # Establecer título de la ventana

# Cargar imágenes
pacman_img = pygame.image.load("pacman.png")
pacman_img = pygame.transform.scale(pacman_img, (TAM_CELDA, TAM_CELDA))  # Escalar la imagen de Pac-Man
fantasma_img = pygame.image.load("fantasma.png")
fantasma_img = pygame.transform.scale(fantasma_img, (TAM_CELDA, TAM_CELDA))  # Escalar la imagen del fantasma

# Función para rotar Pac-Man según la dirección
def obtener_imagen_pacman(pacman_img, direccion):
    if direccion == [1, 0]:  # Derecha
        return pacman_img
    elif direccion == [-1, 0]:  # Izquierda
        return pygame.transform.rotate(pacman_img, 180)
    elif direccion == [0, -1]:  # Arriba
        return pygame.transform.rotate(pacman_img, 90)
    elif direccion == [0, 1]:  # Abajo
        return pygame.transform.rotate(pacman_img, -90)
    return pacman_img

# Crear objetos
pacman = PacMan(14, 23)  # posición inicial de Pac-Man
fantasma = Fantasma(13, 13)  # posición inicial del fantasma
total_pildoras = sum(row.count(2) for row in mapa)

# Bucle principal
ejecutar = True
reloj = pygame.time.Clock()

while ejecutar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False

    # Movimiento autónomo de Pac-Man
    pacman.mover()

    # Movimiento autónomo del fantasma
    fantasma.mover(pacman.pos)

    # Verificar condiciones de victoria o derrota
    if pacman.pos == fantasma.pos:
        print("¡Has sido atrapado por el fantasma! Fin del juego.")
        ejecutar = False

    # Verificar si Pac-Man ha recolectado todas las píldoras
    if pacman.recolectadas == total_pildoras:
        print("¡Has ganado! Has recolectado todas las píldoras.")
        ejecutar = False

    # Dibujar todo
    ventana.fill(AZUL)
    dibujar_mapa(ventana)

    # Obtener la imagen de Pac-Man rotada según su dirección
    pacman_rotado = obtener_imagen_pacman(pacman_img, pacman.direccion)
    ventana.blit(pacman_rotado, (pacman.pos[0] * TAM_CELDA, pacman.pos[1] * TAM_CELDA))

    # Dibujar al fantasma
    ventana.blit(fantasma_img, (fantasma.pos[0] * TAM_CELDA, fantasma.pos[1] * TAM_CELDA))

    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
