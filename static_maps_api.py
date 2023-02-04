import requests


def get_map(*, ll: tuple[float, float], spn: tuple[float, float], map_type: str,
            pt: tuple[object, ...] | str = None) -> str:
    params = requests.get('http://static-maps.yandex.ru/1.x/', params={
        'll': ','.join(map(str, ll)),
        'spn': ','.join(map(str, spn)),
        'l': map_type,
    })
    if pt is not None:
        params['pt'] = ','.join(map(str, pt)) if isinstance(pt, tuple) else pt
    response = requests.get('')

    if not response:
        raise RuntimeError(
            f'''Ошибка выполнения запроса:
            {response.request.url}
            Http статус: {response.status_code} ({response.reason})''')

    filename = 'map.png'
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename
