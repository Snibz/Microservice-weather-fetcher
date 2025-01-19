from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    api_key = 'get out repo rats'# Your openweathermap api key here

    # Fetch latitude and longitude for the given city
    geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}'
    geocode_response = requests.get(geocode_url)
    if geocode_response.status_code != 200 or not geocode_response.json():
        return jsonify({'error': 'Failed to fetch geolocation data'}), geocode_response.status_code

    geocode_data = geocode_response.json()[0]
    lat = geocode_data['lat']
    lon = geocode_data['lon']

    # Fetch weather data using latitude and longitude
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    weather_response = requests.get(weather_url)
    if weather_response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), weather_response.status_code

    weather_data = weather_response.json()

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)