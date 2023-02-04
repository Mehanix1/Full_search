import os
import pygame

from static_maps_api import get_map


def show_map(*, ll: tuple[float, float], spn: tuple[float, float], map_type: str,
             **kwarg: tuple[float, float]) -> None:
    map_filename = get_map(ll=ll, spn=spn, map_type=map_type, **kwarg)
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_filename), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_filename)