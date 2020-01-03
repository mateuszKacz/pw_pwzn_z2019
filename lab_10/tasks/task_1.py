import requests

API_URL = 'https://www.metaweather.com/api/'


def get_cities_woeid(query: str, timeout: float = 5.):

    url = API_URL+'location/search/'
    try:
        response = requests.get(url, params=('query=' + query), timeout=timeout)

        if response.status_code != 200:
            raise requests.exceptions.HTTPError

        response = response.json()

    except RuntimeError as err:
        raise err

    woeid_dict = {}

    for city in response:
        woeid_dict[city['title']] = city['woeid']

    return woeid_dict


if __name__ == '__main__':
    get_cities_woeid('Warszawa')
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
