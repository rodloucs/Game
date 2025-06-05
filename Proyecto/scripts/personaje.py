import pygame
from scripts.configuracion import frame_width,frame_height,ventana_altura,ventana_ancho

class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.timer = 0
        self.animation_speed = 0.1
        self.current_frame = 0
        self.speed=2
        # Primero cargas la imagen completa
        self.spritesheet_stay = pygame.image.load('recursos/imagenes/stay.png').convert_alpha()
        self.spritesheet_run = pygame.image.load('recursos/imagenes/run.png').convert_alpha()
        # Luego llamas a una función que recorte la spritesheet y devuelva la lista de frames
        self.frames_stay = self.animation('recursos/imagenes/stay.png', frame_height, frame_width, columna=3, fila=3, max_frames=9)
        self.frames_run = self.animation('recursos/imagenes/run.png', frame_height, frame_width, columna=3, fila=3, max_frames=8)
        self.frames = self.frames_stay
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=(x, y))

    def animation(self,ruta,ancho,alto,columna,fila,max_frames=None):
        spritesheet = pygame.image.load(ruta).convert_alpha()
        frames = []
        total_frames = columna * fila if max_frames is None else max_frames

        for fila in range(fila):
            for columna in range(columna):
                if len(frames) >= total_frames:
                    return frames
                frame = spritesheet.subsurface((columna * ancho, fila * alto, ancho, alto))
                frames.append(frame)
        return frames

    def update(self, dt, keys):
        dx = dy = 0

        if keys[pygame.K_RIGHT]:
            dx = self.speed
        elif keys[pygame.K_LEFT]:
            dx = -self.speed

        if keys[pygame.K_DOWN]:
            dy = self.speed
        elif keys[pygame.K_UP]:
            dy = -self.speed

        en_movimiento = dx != 0 or dy != 0

        # Cambiar animación
        if en_movimiento:
            if self.frames != self.frames_run:
                self.frames = self.frames_run
                self.current_frame = 0
                self.timer = 0
        else:
            if self.frames != self.frames_stay:
                self.frames = self.frames_stay
                self.current_frame = 0
                self.timer = 0

        # Actualizar frame de animación
        self.timer += dt
        if self.timer >= self.animation_speed:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

        # Movimiento
        self.rect.x += dx
        self.rect.y += dy

        # Límite de pantalla (opcional)
        self.rect.clamp_ip(pygame.Rect(10,0,ventana_ancho, ventana_altura))
