"""
Weather Forecast FastAPI Application

This is a FastAPI application for retrieving weather forecasts based on specified parameters.
"""


from fastapi import FastAPI, HTTPException, Query

from services import WeatherRequest, request_processing
from validators import is_valid_latitude, is_valid_longitude

app = FastAPI()


@app.get('/getForecast', response_model=dict[int, dict[str, float]])
def get_forecast(
    from_ts: int = Query(...,
                         description="Start time in timestamp format (integer)"),
    to_ts: int = Query(...,
                       description="End time in timestamp format (integer)"),
    lat: float = Query(..., description="Latitude (floating-point number)"),
    lon: float = Query(..., description="Longitude (floating-point number)")
) -> dict[int, dict[str, float]]:
    """
    Get weather forecast for the specified parameters.

    :param from_ts: Start time in timestamp format (integer).
    :param to_ts: End time in timestamp format (integer).
    :param lat: Latitude (floating-point number).
    :param lon: Longitude (floating-point number).

    :return: A dictionary containing weather forecast data with time labels (timestamps) as keys and values as dictionaries
             with temperature (temp).
    """
    if not is_valid_latitude(lat) or not is_valid_longitude(lon):
        raise HTTPException(
            status_code=400, detail="Invalid latitude or longitude")

    try:
        request_weather_data = WeatherRequest(from_ts, to_ts, lat, lon)
        response_weather_data = request_processing(request_weather_data)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return response_weather_data


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
