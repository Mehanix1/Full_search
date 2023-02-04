from math import (
    radians,
    cos,
    sqrt,
)


def find_distance(point_a: tuple[float, float], point_b: tuple[float, float]) -> float:
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = point_a
    b_lon, b_lat = point_b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = radians((a_lat + b_lat) / 2.)
    lat_lon_factor = cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    return sqrt(dx ** 2 + dy ** 2)
