import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London," \
          "us&appid=b6907d289e10d714a6e88b30761fae22 "


def get_weather_data():
    response = requests.get(API_URL)
    return response.json()


def get_temperature(data, timestamp):
    # Extract temperature data for the given timestamp
    for entry in data['list']:
        if entry['dt'] == timestamp:
            return entry['main']['temp']
    return None


def get_wind_speed(data, timestamp):
    # Extract wind speed data for the given timestamp
    for entry in data['list']:
        if entry['dt'] == timestamp:
            return entry['wind']['speed']
    return None


def get_pressure(data, timestamp):
    # Extract pressure data for the given timestamp
    for entry in data['list']:
        if entry['dt'] == timestamp:
            return entry['main']['pressure']
    return None


def main():
    data = get_weather_data()

    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting program...")
            break
        elif choice in [1, 2, 3]:
            timestamp = int(input("Enter the timestamp (dt) for the data you want to fetch: "))
            if choice == 1:
                temp = get_temperature(data, timestamp)
                print(f"Temperature at timestamp {timestamp}: {temp}")
            elif choice == 2:
                wind_speed = get_wind_speed(data, timestamp)
                print(f"Wind Speed at timestamp {timestamp}: {wind_speed}")
            elif choice == 3:
                pressure = get_pressure(data, timestamp)
                print(f"Pressure at timestamp {timestamp}: {pressure}")
            else:
                print("Invalid choice. Please choose again.")
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
