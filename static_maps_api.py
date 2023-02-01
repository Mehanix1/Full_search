import requests


def get_map(ll: tuple[float, float], spn: tuple[float], map_type: str) -> str:
    response = requests.get('http://geocode-maps.yandex.ru/1.x/', params={
        'll': ','.join(map(str, ll)),
        'spn': ','.join(map(str, ll)),
        'l': spn,
    })

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
                {response.request}
                Http статус: {response.status_code} ({response.reason})'''
        )

    filename = 'map.png'
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename
