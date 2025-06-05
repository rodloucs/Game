import pygame
from scripts.configuracion import ventana_altura, ventana_ancho, RGB, fps
from scripts.personaje import Personaje
from scripts.mascota import Mascota

def main():
    # Inicializar pygame
    pygame.init()
    # Creación de la ventana y reloj
    ventana = pygame.display.set_mode((ventana_ancho, ventana_altura))
    reloj = pygame.time.Clock()
    # Crear al personaje y grupo de sprites
    personaje = Personaje(20,0)
    mascota = Mascota(0,10)
    grupo = pygame.sprite.Group(personaje)
    grupo2 = pygame.sprite.Group(mascota)

    # Estado del juego
    estado = True

    while estado:
        dt = reloj.tick(fps) / 1000  # Delta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False

        keys = pygame.key.get_pressed()  # Capturar estado actual del teclado

        personaje.update(dt, keys)       # Actualizar personaje con dt y teclas
        mascota.update(dt,keys)                # Actualizar mascota con dt
        ventana.fill(RGB)
        grupo.draw(ventana)
        grupo2.draw(ventana)
        pygame.display.flip()

    pygame.quit()
