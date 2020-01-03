import pathlib
from typing import Optional, Union, List
import requests
import pandas as pd

API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):

    _file_paths = []
    data = []
    woeid = str(woeid)
    year = str(year)
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    city_year_month = woeid + '_' + year + '_' + month

    if path:
        _dir_path = pathlib.Path.cwd() / path / city_year_month

    else:
        _dir_path = pathlib.Path.cwd() / city_year_month

    try:
        pathlib.Path.mkdir(_dir_path)
    except FileExistsError as err:
        print(err)

    for day in range(1, 32):

        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)

        url = API_URL + 'location/' + woeid + '/' + year + '/' + month + '/' + day
        try:

            response = requests.get(url, timeout=timeout)
            if response.status_code != 200:
                raise requests.exceptions.HTTPError

            response = response.json()
            print(f'Downloaded{day}')

            _file_paths.append(_dir_path / city_year_month)

            data.append(response[0])

        except RuntimeError as err:
            raise err
    frame = pd.DataFrame(data)
    frame.set_index('created')
    frame = frame[['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility',
                'wind_direction_compass', 'wind_direction', 'wind_speed']]
    frame['created'] = frame['created'].apply(lambda x: str(x)[:16])
    frame = frame.rename({'the_temp': 'temp'}, axis=1)
    frame.to_csv(str(_dir_path) + '/' + (city_year_month + '.csv'), index=False)

    return _dir_path, _file_paths


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
