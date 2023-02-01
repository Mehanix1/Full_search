import requests


def get_coordinates(address: str) -> tuple[float | None, float | None]:
    toponym = geocoder_request(address)
    if toponym is None:
        return None, None

    # Координаты центра топонима:
    toponym_coodrinates = toponym['Point']['pos']
    # Широта, преобразованная в плавающее число:
    toponym_longitude, toponym_lattitude = map(float, toponym_coodrinates.split(' '))
    return toponym_longitude, toponym_lattitude


def get_coordinates_and_span(address: str) -> tuple[tuple[float | None, float | None], tuple[float | None, float | None]]:
    toponym = geocoder_request(address)
    if toponym is None:
        return (None, None), (None, None)

    # Координаты центра топонима:
    toponym_coodrinates = toponym['Point']['pos']
    # Широта, преобразованная в плавающее число:
    toponym_longitude, toponym_lattitude = map(float, toponym_coodrinates.split(' '))

    # Рамка вокруг объекта:
    envelope = toponym['boundedBy']['Envelope']
    # левая, нижняя, правая и верхняя границы из координат углов:
    l, b = map(float, envelope['lowerCorner'].split())
    r, t = map(float, envelope['upperCorner'].split())
    # Вычисляем полуразмеры по вертикали и горизонтали
    dx = abs(l - r) / 2
    dy = abs(t - b) / 2

    return (toponym_longitude, toponym_lattitude), (dx, dy)


API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocoder_request(address: str) -> dict | None:
    # Выполняем запрос.
    response = requests.get('http://geocode-maps.yandex.ru/1.x/', params={
        'apikey': API_KEY,
        'geocode': address,
        'format': 'json',
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
            {response.request.url}
            Http статус: {response.status_code} ({response.reason})''')

    # Преобразуем ответ в json-объект
    data = response.json()
    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа он находится по следующему пути:
    features = data['response']['GeoObjectCollection']['featureMember']
    return features[0]['GeoObject'] if features else None
