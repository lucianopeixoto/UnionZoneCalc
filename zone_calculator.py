import sys
import requests
import configparser
import math

# Toronto City Hall coordinates
CITY_HALL_LAT = 43.65352152565906
CITY_HALL_LNG = -79.38405043405932


def load_api_key():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    return config["google"]["api_key"]


def get_address_from_input():
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    else:
        return input("Enter address: ")


def geocode_address(address, api_key):
    url = f"https://geocode.googleapis.com/v4/geocode/address/{requests.utils.quote(address)}"
    params = {"key": api_key}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed: {response.text}")

    data = response.json()

    if not data.get("results"):
        raise Exception("No results found for address")

    location = data["results"][0]["location"]
    return location["latitude"], location["longitude"], data["results"][0]["formattedAddress"]


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def determine_zone(distance_km, lat):
    notes = []

    # Special case: south of Lake Ontario (rough approximation)
    if lat < 43.60:
        return "Room & Board", distance_km, ["Location appears south of Lake Ontario → Treat as Room & Board"]

    # Zone logic
    if distance_km <= 20:
        zone = "Zone 1"
    elif distance_km <= 50:
        zone = "Zone 3"
    elif distance_km <= 80:
        zone = "Zone 4"
    elif distance_km <= 95:
        zone = "Zone 5"
    else:
        zone = "Outside defined zones"

    # Toronto Islands note
    if 2.2 <= distance_km <= 3.4:
        notes.append("If this location is on Toronto Islands → verify manually for Zone 2")

    return zone, distance_km, notes


def main():
    try:
        address = get_address_from_input()
        api_key = load_api_key()

        lat, lng, formatted = geocode_address(address, api_key)

        distance = haversine(CITY_HALL_LAT, CITY_HALL_LNG, lat, lng)

        zone, distance_km, notes = determine_zone(distance, lat)

        print("\n--- RESULT ---")
        print(f"Address: {formatted}")
        print(f"Coordinates: {lat}, {lng}")
        print(f"Distance from City Hall: {distance_km:.2f} km")
        print(f"Zone: {zone}")

        if notes:
            print("\nNotes:")
            for note in notes:
                print(f"- {note}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
