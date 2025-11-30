import pygame
import sys
import os

# --- Centramos la ventana ---
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Inicializar Pygame
pygame.init()

# Tamaños de pantalla
MENU_WIDTH = 300
MENU_HEIGHT = 200
GAME_WIDTH = 350
GAME_HEIGHT = 350  # Aumentamos la altura para tener espacio para el piso

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configuración inicial (pantalla pequeña - menú)
screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
pygame.display.set_caption("Menú principal")

# Fuente
font = pygame.font.SysFont(None, 40)

# Botón iniciar
button_width = 180
button_height = 60
button_x = MENU_WIDTH // 2 - button_width // 2
button_y = MENU_HEIGHT // 2 - button_height // 2
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Clock
clock = pygame.time.Clock()

# Variables del juego
game_started = False
sprite_size = 40
sprite = pygame.Surface((sprite_size, sprite_size))
sprite.fill(RED)  # Cambiamos a rojo para mejor visibilidad
sprite_x = 0
sprite_y = 0
speed = 4

# Variables de física
gravity = 0.5
jump_strength = -10
vertical_velocity = 0
is_jumping = False
is_on_ground = False

# Piso
floor_height = 50
floor_y = GAME_HEIGHT - floor_height

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar click en el botón
        if not game_started and event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Cambiar a juego (pantalla más grande)
                os.environ["SDL_VIDEO_CENTERED"] = "1"  # centrar de nuevo
                screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
                pygame.display.set_caption("Juego iniciado")
                game_started = True
                sprite_x = GAME_WIDTH // 2 - sprite_size // 2
                sprite_y = floor_y - sprite_size  # Colocar sobre el piso

        # Detectar salto (barra espaciadora)
        if game_started and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and is_on_ground:
                vertical_velocity = jump_strength
                is_jumping = True
                is_on_ground = False

    # ----------- MENÚ -----------
    if not game_started:
        screen.fill(WHITE)

        # Cambiar color si el mouse está encima
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, DARK_GRAY, button_rect)
        else:
            pygame.draw.rect(screen, GRAY, button_rect)

        text = font.render("Iniciar Juego", True, BLACK)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    # ----------- JUEGO -----------
    else:
        # Movimiento horizontal
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            sprite_x -= speed
        if keys[pygame.K_d]:
            sprite_x += speed

        # Aplicar gravedad
        vertical_velocity += gravity
        sprite_y += vertical_velocity

        # Detectar colisión con el piso
        if sprite_y >= floor_y - sprite_size:
            sprite_y = floor_y - sprite_size
            vertical_velocity = 0
            is_on_ground = True
            is_jumping = False
        else:
            is_on_ground = False

        # Limitar movimiento horizontal dentro de la pantalla
        if sprite_x < 0:
            sprite_x = 0
        elif sprite_x > GAME_WIDTH - sprite_size:
            sprite_x = GAME_WIDTH - sprite_size

        # Dibujar todo
        screen.fill(WHITE)
        
        # Dibujar piso
        pygame.draw.rect(screen, GREEN, (0, floor_y, GAME_WIDTH, floor_height))
        
        # Dibujar sprite
        screen.blit(sprite, (sprite_x, sprite_y))
        
        # Mostrar información (opcional)
        info_text= f"VelY: {vertical_velocity:.1f} Suelo: {is_on_ground}"
        info_surface = pygame.font.SysFont(None, 20).render(info_text, True, BLACK)
        screen.blit(info_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit