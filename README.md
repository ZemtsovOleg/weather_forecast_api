# Weather Forecast FastAPI Application

This is a FastAPI application for retrieving weather forecasts based on specified parameters.

## Installation

1. Clone the repository:

<pre lang="bash">git clone <repository_url>
cd weather_forecast_api</pre>

2. Install the dependencies:

<pre lang="bash">pip install -r requirements.txt</pre>

## Usage
Start the FastAPI server:

<pre lang="bash">uvicorn main:app --host 0.0.0.0 --port 8000</pre>

Make GET requests to retrieve weather forecasts:

<pre lang="bash">
curl -X 'GET' \
  'http://localhost:8000/getForecast?from_ts=1580886675&to_ts=1580886680&lat=37.7749&lon=-122.4194' \
  -H 'accept: application/json' </pre>

Replace the query parameters (from_ts, to_ts, lat, and lon) with your desired values.


## API Documentation
The API provides the following endpoint:

/getForecast: Retrieve weather forecasts based on specified parameters.
## Request Parameters
from_ts (integer): Start time in timestamp format.
to_ts (integer): End time in timestamp format.
lat (float): Latitude in decimal degrees.
lon (float): Longitude in decimal degrees.
## Response
The response is a JSON object containing weather forecast data with timestamps as keys and temperature values as values.

Example response:

<pre lang="bash">
{
    1580886675: {
        "temp": 286.248944
    },
    1580886676: {
        "temp": 287.0
    },
    1580886677: {
        "temp": 288.0
    }
}
</pre>