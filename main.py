from db_connection import save, load
from read_weather_api import read_todays_weather, request_past_data
from datetime import datetime


def main():
    data = load()
    if (len(data) > 0) and (data[0].date.date() == datetime.now().date()):
        print("You have already registered today's weather")
        if input("Do you want to register it again? [y/N]: ").strip().lower() == 'n':
            return

    print("Reading api...")
    weather_data = request_past_data(data[0].date.date())
    weather_data.append(read_todays_weather())

    print("Saving data in database...")
    save(weather_data)

    print("Today's weather saved successfully")


if __name__ == "__main__":
    print("Starting weather tracker program...")
    main()
