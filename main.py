from db_connection import save, load
from weather import Weather
from read_weather_api import read_weather
from datetime import datetime
from colorama import init as init_colorama, Fore, Style
from typing import Literal
import sys


def show_error(msg: str = "Invalid input"):
    print(Fore.RED + msg + Style.RESET_ALL)


def get_int_input(msg: str, err_msg: str = "Invalid input"):
    data = ''
    while not data.isdigit():
        data = input(msg).strip()
        if not data.isdigit():
            show_error(err_msg)
    return int(data)


def input_weather() -> Weather:
    max_temp = get_int_input("Enter today's maximum temperature in Celcius: ")
    min_temp = get_int_input("Enter today's minimum temperature in Celcius: ")
    humidity = get_int_input(
        "Enter today's humidity percentage (ommit the '%'): "
    )
    date = datetime.now()

    return Weather(
        max=max_temp,
        min=min_temp,
        air_humidity=humidity,
        date=date
    )


def main(mode: Literal["manual", "auto"]):
    data = load()
    if (len(data) > 0) and (data[-1].date.date() == datetime.now().date()):
        print("You have already registered today's weather")

        if mode == "auto":
            return

        if input("Do you want to register it again? [y/N]: ").strip().lower() == 'n':
            return

    if mode == "auto":
        print("Reading api...")
        weather = read_weather()
    else:
        weather = input_weather()

    print("Saving data in database...")
    save(weather)

    print("Today's weather saved successfully")


if __name__ == "__main__":
    init_colorama()

    mode = sys.argv[1] if len(sys.argv) > 1 else "auto"
    main(mode)
