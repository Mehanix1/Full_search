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


API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocoder_request(address: str) -> dict:
    response = requests.get('http://geocode-maps.yandex.ru/1.x/', params={
        'apikey': API_KEY,
        'geocode': address,
        'format': 'json'
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
