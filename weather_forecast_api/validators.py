def is_valid_latitude(latitude: float) -> bool:
    """
    Check if the given latitude value is valid.

    :param latitude: The latitude value to check.
    :return: True if the value is valid, False otherwise.
    """
    return -90.0 <= latitude <= 90.0


def is_valid_longitude(longitude: float) -> bool:
    """
    Check if the given longitude value is valid.

    :param longitude: The longitude value to check.
    :return: True if the value is valid, False otherwise.
    """
    return -180.0 <= longitude <= 180.0
