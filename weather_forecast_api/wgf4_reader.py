import struct
from pathlib import Path
from typing import Union

import numpy as np
from calculate_offset import calculate_offset
from settings import DATA_FOLDER


def read_wgf4_file(file_name: str, request_weather_data) -> Union[float, None]:
    """
    Read a weather data file in WGF4 format and retrieve the temperature data at the specified coordinates.

    :param file_name: The name of the WGF4 file to read.
    :param request_weather_data: An instance of WeatherRequest containing request parameters.
    :return: The temperature value at the specified coordinates, or None if data is not available.
    :raises ValueError: If the coordinates are invalid.
    """
    file_path = Path(DATA_FOLDER) / file_name
    with open(file_path, 'rb') as fp:
        header_str = fp.read(8 * 4)
        header_values = struct.unpack("7i1f", header_str)
        offset = calculate_offset(header_values, request_weather_data)

        chunk_size = 1024
        temp = None

        while True:
            data = fp.read(chunk_size * 4)
            if not data:
                break
            float_values = np.frombuffer(data, dtype=np.float32)

            if offset < len(float_values):
                temp = float_values[offset]
                if temp != -100500.0:
                    return temp

            offset -= len(float_values)

    raise ValueError(
        "Invalid coordinates: Data not available for the specified coordinates")
