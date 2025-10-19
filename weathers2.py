import requests

def get_coordinates(city_name):
    """Get latitude and longitude of a city using OpenStreetMap API"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city_name, "format": "json", "limit": 1}
    headers = {"User-Agent": "PythonPracticeApp/1.0 (contact: test@example.com)"}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    if data:
        return float(data[0]["lat"]), float(data[0]["lon"])
    else:
        raise ValueError(f"City '{city_name}' not found.")


def get_weather(lat, lon):
    """Get temperature (°C) and windspeed (km/h) from Open-Meteo API"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    weather = data.get("current_weather", {})

    temp = weather.get("temperature")
    wind = weather.get("windspeed")

    if temp is None or wind is None:
        raise ValueError("Weather data not available for this location.")

    # convert m/s → km/h and round
    wind = round(wind * 3.6, 1)
    return temp, wind


def compare_cities_weather(city1, city2):
    """Compare two cities' temperatures and wind speeds"""
    lat1, lon1 = get_coordinates(city1)
    lat2, lon2 = get_coordinates(city2)

    temp1, wind1 = get_weather(lat1, lon1)
    temp2, wind2 = get_weather(lat2, lon2)

    diff = temp1 - temp2

    return {
        "city1": {"name": city1, "temp": temp1, "wind": wind1},
        "city2": {"name": city2, "temp": temp2, "wind": wind2},
        "diff": diff
    }


def main():
    try:
        city1 = input("Enter first city: ").strip().title()
        city2 = input("Enter second city: ").strip().title()

        if not city1 or not city2:
            raise ValueError("Please enter valid city names.")

        result = compare_cities_weather(city1, city2)

        print(f"\n🌤 {result['city1']['name']}: {result['city1']['temp']}°C, wind {result['city1']['wind']} km/h")
        print(f"🌤 {result['city2']['name']}: {result['city2']['temp']}°C, wind {result['city2']['wind']} km/h")

        diff = result["diff"]
        if diff > 0:
            print(f"\n🔥 {city1} is {diff:.1f}°C warmer than {city2}.")
        elif diff < 0:
            print(f"\n❄️ {city2} is {abs(diff):.1f}°C warmer than {city1}.")
        else:
            print("\n🌈 Both cities have the same temperature.")

        mode = input("\nShow temperatures in Fahrenheit too? (y/n): ").lower()
        if mode == "y":
            f1 = result["city1"]["temp"] * 9/5 + 32
            f2 = result["city2"]["temp"] * 9/5 + 32
            print(f"\n{city1}: {f1:.1f}°F")
            print(f"{city2}: {f2:.1f}°F")

    except requests.exceptions.RequestException:
        print("⚠️ Network or connection error.")
    except ValueError as e:
        print("⚠️", e)
    except KeyError:
        print("⚠️ Weather data not found in API response.")


if __name__ == "__main__":
    main()
