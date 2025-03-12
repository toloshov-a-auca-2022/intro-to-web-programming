# Example 2: Exposing an API (Conceptual Overview)
# Consider a scenario where you want to allow other applications to interact with your weather service. You might create an API endpoint that returns weather data for a given city. In a simple web framework like Flask, it might look like this:

from flask import Flask, jsonify, request
app = Flask(__name__)

weatherData = {
    "New York": {"temperature": 28, "condition": "Sunny"},
    "London": {"temperature": 15, "condition": "Rainy"},
    "Paris": {"temperature": 20, "condition": "Cloudy"},
}

@app.route("/")
def index():
    return jsonify(weatherData)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city in weatherData:
        return jsonify({city: weatherData[city]})
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)