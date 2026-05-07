import pygame
import random
import math

# --- НАСТРОЙКИ ---
WIDTH = 480
HEIGHT = 800
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Global Survivors Resist")
clock = pygame.time.Clock()

# --- ПЕРЕМЕННЫЕ ИГРЫ ---
score = 0
gold = 0
level = 1

# Параметры игрока (можно улучшать)
player_speed = 5
bullet_speed = 10
fire_rate = 500  # мс между выстрелами
bullet_size = 5

# --- КЛАССЫ ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += player_speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= player_speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += player_speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > fire_rate:
            self.last_shot = now
            # Автострельба в ближайшего врага
            if enemies:
                target = min(enemies, key=lambda e: math.hypot(e.rect.centerx - self.rect.centerx, e.rect.centery - self.rect.centery))
                bullet = Bullet(self.rect.center, target.rect.center)
                all_sprites.add(bullet)
                bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, WIDTH - 30)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos):
        super().__init__()
        self.image = pygame.Surface((bullet_size, bullet_size))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=start_pos)
        
        # Расчет направления
        angle = math.atan2(target_pos[1] - start_pos[1], target_pos[0] - start_pos[0])
        self.dx = math.cos(angle) * bullet_speed
        self.dy = math.sin(angle) * bullet_speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if not screen.get_rect().contains(self.rect):
            self.kill()

# --- ГРУППЫ СПРАЙТОВ ---
all_sprites = pygame.sprite.Group()
enemies
