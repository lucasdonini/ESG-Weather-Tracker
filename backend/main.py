from db_connection import save, load
from read_weather_api import read_weather_api
from datetime import datetime, timedelta


def main():
    data = load()
    start_date = datetime.fromisoformat("2026-02-09").date() if len(data) == 0 else data[0].date.date() + timedelta(days=1)
    end_date = datetime.now().date() - timedelta(days=1)
    
    if len(data) > 0 and start_date > end_date:
        print("You have already registered past weather")
        return

    print("Reading api...")
    weather_data = read_weather_api(start_date=start_date, end_date=end_date)

    print("Saving data in database...")
    save(weather_data)

    print("Past weather saved successfully")


if __name__ == "__main__":
    print("Starting weather tracker program...")
    main()
