# Weather Forecast FastAPI Application

This is a FastAPI application for retrieving weather forecasts based on specified parameters.

## Requirements:

- Python (version 3.11 or higher)
- Other dependencies specified in `requirements.txt`

## Installation

1. Clone the repository:

<pre lang="bash">git clone https://github.com/ZemtsovOleg/weather_forecast_api.git</pre>

2. Go to the project folder:

<pre lang="bash">cd weather_forecast_api</pre>

3. Install the dependencies:

<pre lang="bash">pip install -r requirements.txt</pre>

## Usage

Go to the project folder:

<pre lang="bash">cd weather_forecast_api</pre>

Start the FastAPI server:

<pre lang="bash">uvicorn main:app --host 0.0.0.0 --port 80</pre>

### Getting Weather Forecasts

To obtain a weather forecast, send a GET request to the `http://localhost/getForecast` endpoint with the following parameters:

- `from_ts` - start time in timestamp format (integer).
- `to_ts` - end time in timestamp format (integer).
- `lat` - latitude (floating-point number).
- `lon` - longitude (floating-point number).

Example request:

```
http://localhost/getForecast?from_ts=1631952000&to_ts=1632042000&lat=52.5200&lon=13.4050
```

Replace the query parameters (from_ts, to_ts, lat, and lon) with your desired values.

## API Documentation

The API provides the following endpoint:

/getForecast: Retrieve weather forecasts based on specified parameters.

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

<br>

# Running in a Docker Container

## Requirements

- Docker (for running in a container)

## Building the Docker Container

1. Build the Docker container:

```bash
docker build -t weather_forecast_api .
```

## Running in a Docker Container

2. Start the container using Docker Compose:

```bash
docker-compose up -d
```

3. The API will be available at `http://localhost`.

Note: Make sure to install Docker and Docker Compose before running the containerized application.