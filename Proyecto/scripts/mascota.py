import pygame
from scripts.configuracion import frame_width,frame_height
from .personaje import Personaje
class Mascota(Personaje):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.spritesheet_stay = pygame.image.load('recursos/imagenes/llama.png').convert_alpha()
        self.spritesheet_run = pygame.image.load('recursos/imagenes/llama.png').convert_alpha()
        # Luego llamas a una función que recorte la spritesheet y devuelva la lista de frames
        self.frames_stay = self.animation('recursos/imagenes/llama.png', frame_height, frame_width, columna=2, fila=3, max_frames=6)
        self.frames_run = self.animation('recursos/imagenes/llama.png', frame_height, frame_width, columna=2, fila=3, max_frames=6)
        