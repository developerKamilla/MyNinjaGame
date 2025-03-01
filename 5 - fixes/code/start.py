import pygame
import os
import sys
from main import Game  # Импортируем функцию для запуска игры

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Button:
    def __init__(self, text, x, y, width, height):
        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)
        self.hover_color = (0, 200, 0)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]

def show_menu():
    clock = pygame.time.Clock()
    start_button = Button("Старт", 250, 150, 100, 50)
    instructions = "Нажмите 'Старт', чтобы начать игру."

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 255))  # Заливка фона
        start_button.draw(screen)

        # Отображение инструкций
        font = pygame.font.Font(None, 24)
        instructions_surface = font.render(instructions, True, (255, 255, 255))
        screen.blit(instructions_surface, (150, 100))

        if start_button.is_clicked():
            running = False  # Закрываем меню, чтобы запустить игру

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    show_menu()