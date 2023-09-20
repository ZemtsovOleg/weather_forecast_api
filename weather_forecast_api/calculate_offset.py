def convert_header_values(header_values: tuple) -> tuple:
    """
    Convert header values to meaningful coordinates and grid steps.

    :param header_values: A tuple containing header values.
    :return: A tuple containing (min_lat, min_lon, max_lon, grid_step_lat, grid_step_lon).
    """
    minY, _, minX, maxX, dy, dx, multiplier, _ = header_values

    min_lat = minY / multiplier
    min_lon = minX / multiplier
    max_lon = maxX / multiplier
    grid_step_lat = dy / multiplier
    grid_step_lon = dx / multiplier

    return min_lat, min_lon, max_lon, grid_step_lat, grid_step_lon


def calculate_offset(header_values: tuple, request_weather_data) -> int:
    """
    Calculate the data offset based on header values and request coordinates.

    :param header_values: A tuple containing header values.
    :param request_weather_data: An instance of WeatherRequest containing request parameters.
    :return: The calculated offset.
    :raises ValueError: If the provided coordinates are outside the valid range.
    """
    minY, minX, maxX, dy, dx = convert_header_values(header_values)

    lat_index = int((request_weather_data.lat - minY) / dy)
    lon_index = int((request_weather_data.lon - minX) / dx)

    offset = (lat_index * int((maxX - minX) / dx) + lon_index) * 4

    return offset
