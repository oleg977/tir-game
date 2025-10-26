import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тир")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Шрифт для счета
font = pygame.font.Font(None, 36)

# Класс для мишени
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

# Группа спрайтов
targets = pygame.sprite.Group()

# Функция для создания новой мишени
def create_target():
    target = Target()
    targets.add(target)

# Основные переменные
score = 0
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка попадания по мишени
            pos = pygame.mouse.get_pos()
            for target in targets:
                if target.rect.collidepoint(pos):  # Проверяем, попал ли клик в мишень
                    target.kill()  # Удаляем мишень
                    score += 1
                    create_target()

    # Создание новой мишени, если их нет
    if len(targets) == 0:
        create_target()

    # Отрисовка мишеней
    targets.draw(screen)

    # Отрисовка счета
    score_text = font.render(f"Счет: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

# Завершение Pygame
pygame.quit()
sys.exit()