import os

from settings import DATA_FOLDER
from wgf4_reader import read_wgf4_file


class WeatherRequest:
    def __init__(
        self, from_ts: int, to_ts: int, lat: float, lon: float
    ) -> None:
        """
        Initializes a WeatherRequest object.

        :param from_ts: Start time in timestamp format (integer).
        :param to_ts: End time in timestamp format (integer).
        :param lat: Latitude (floating-point number).
        :param lon: Longitude (floating-point number).
        """
        self.from_ts = from_ts
        self.to_ts = to_ts
        self.lat = lat
        self.lon = lon


def request_processing(request_weather_data: WeatherRequest) -> dict:
    """
    Processes a weather data request.

    :param request_weather_data: An instance of WeatherRequest containing request parameters.
    :return: A dictionary containing weather forecast data with time labels (timestamps) as keys and values as dictionaries
             with temperature (temp).
    """
    file_list = find_files_by_timestamps(request_weather_data)
    response_weather_data = fetch_temperature_data_from_files(
        file_list, request_weather_data)

    return response_weather_data


def fetch_temperature_data_from_files(
        file_list: list[str], request_weather_data: WeatherRequest
) -> dict[int, dict[str, float]]:
    """
    Fetch temperature data from a list of weather data files.

    :param file_list: List of file names to process.
    :param request_weather_data: An instance of WeatherRequest containing request parameters.
    :return: A dictionary containing weather forecast data with time labels (timestamps) as keys and values as dictionaries
             with temperature (temp).
    """
    response_weather_data = {}

    for file_name in file_list:
        temp = read_wgf4_file(file_name, request_weather_data)
        timestamp = int(file_name.split(".")[0])
        response_weather_data[timestamp] = {"temp": temp}

    return response_weather_data


def find_files_by_timestamps(request_weather_data: WeatherRequest) -> list:
    """
    Finds weather data files based on timestamp range and coordinates.

    :param request_weather_data: An instance of WeatherRequest containing request parameters.
    :return: A list of file names that match the specified criteria.
    :raises FileNotFoundError: If no matching files are found.
    """
    file_list = []

    for file_name in os.listdir(DATA_FOLDER):
        if file_name.endswith(".wgf4"):

            timestamp = int(file_name.split(".")[0])
            if request_weather_data.from_ts <= timestamp <= request_weather_data.to_ts:
                file_list.append(file_name)

    if not file_list:
        raise FileNotFoundError("File not found")
    return file_list
