from db_connection import load
from weather import Weather
from typing import List, TypedDict
from datetime import date
from collections import defaultdict
import matplotlib.pyplot as plt


class NormalizedWeatherData(TypedDict):
    min_temp: List[float]
    max_temp: List[float]
    air_humidity: List[float]
    date: List[date]


def normalize_data(data: List[Weather]) -> NormalizedWeatherData:
    normalized: NormalizedWeatherData = defaultdict(list)

    for entry in data[::-1]:
        normalized['min_temp'].append(entry.min)
        normalized['max_temp'].append(entry.max)
        normalized['air_humidity'].append(entry.air_humidity)
        normalized['date'].append(f'{entry.date.day}/{entry.date.month}')
    return normalized


def plot_graph(data: NormalizedWeatherData):
    date = data['date']

    plt.figure(figsize=(10, 6))

    plt.plot(date, data['min_temp'], label='Temperatura Mínima (C°)', linestyle='-', color='green')
    plt.plot(date, data['max_temp'], label='Temperatura Máxima (C°)', linestyle='-', color='red')
    plt.plot(date, data['air_humidity'], label='Humidade do Ar (%)', linestyle='-', color='blue')

    plt.title('Monitoramento do clima - ESG', fontsize=14)
    plt.xlabel('Data')
    plt.grid(True, linestyle='-', alpha=0.6)
    plt.margins(x=0)
    plt.legend()

    plt.savefig('results.png')


def main():
    raw_data = load()
    normalized = normalize_data(raw_data)
    plot_graph(normalized)


if __name__ == '__main__':
    main()
