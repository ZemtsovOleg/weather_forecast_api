import struct
from pathlib import Path

import numpy as np

from calculate_offset import calculate_offset
from settings import DATA_FOLDER


def read_wgf4_file(file_name: str, request_weather_data) -> float:
    """
    Read a weather data file in WGF4 format and retrieve the temperature data at the specified coordinates.

    :param file_name: The name of the WGF4 file to read.
    :param request_weather_data: An instance of WeatherRequest containing request parameters.
    :return: The temperature value at the specified coordinates.
    :raises ValueError: If the coordinates are invalid or data is not available.
    """
    file_path = Path(DATA_FOLDER) / file_name
    with open(file_path, 'rb') as fp:

        header_str = fp.read(8 * 4)
        header_values = struct.unpack("7i1f", header_str)

        offset = calculate_offset(header_values, request_weather_data)
        float_values = np.fromfile(fp, dtype=np.float32)

        if offset >= len(float_values):
            raise ValueError(
                "Invalid coordinates: Data not available for the specified coordinates")

        return float_values[offset]
