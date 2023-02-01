import os
from sys import argv
import pygame

from geocoder_api import (
    get_coordinates,
    get_coordinates_and_span,
)
from static_maps_api import get_map


def main() -> None:
    toponym_to_find = ' '.join(argv[1:])

    if toponym_to_find == '':
        print('No data')
        return

    # Показываем карту с фиксированным масштабом.
    lat, lon = get_coordinates(toponym_to_find)
    show_map(ll=(lat, lon), spn=(0.005, 0.005), map_type='map')

    # Показываем карту с масштабом, подобранным по заданному объекту.
    (lat, lon), (dx, dy) = get_coordinates_and_span(toponym_to_find)
    show_map(ll=(lat, lon), spn=(dx, dy), map_type='map')


def show_map(*, ll: tuple[float, float], spn: tuple[float, float], map_type: str,
             **kwargs: tuple[float, float]) -> None:
    map_filename = get_map(ll=ll, spn=spn, map_type=map_type, **kwargs)
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


main()
