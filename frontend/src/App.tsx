import ky from "ky";
import { useEffect, useState } from "react";
import "./App.css";
import WeatherChart from "./WeatherChart";

interface Weather {
  date: string;
  min: number;
  max: number;
  air_humidity: number;
}

function App() {
  const [data, setData] = useState<Weather[]>([]);
  const [loaded, setLoaded] = useState(true);

  useEffect(() => {
    const baseUrl = import.meta.env.VITE_API_URL
    const endpoint = `${baseUrl ?? ""}/api/load`
    console.log("Requested endpoint:", endpoint)
    ky.get(endpoint)
      .json<Weather[]>()
      .then(setData)
      .catch((e) => {
        console.error("Failed to fetch data from backend: ", e);
        setLoaded(false);
      });
  }, []);

  const normalizedDates = data.map(entry => {
    const date = new Date(entry.date)
    const day = date.getUTCDate()
    const month = date.getUTCMonth() + 1
    return `${day}/${month}`
  })

  return (
  <div id="app-wrapper">
    <div id="chart-area">
      {(loaded && (
        <WeatherChart
          dates={normalizedDates}
          min_temps={data.map((entry) => entry.min)}
          max_temps={data.map((entry) => entry.max)}
          humidities={data.map((entry) => entry.air_humidity)}
        />
      )) || <p>Something went wrong</p>}
    </div>
    <footer id="app-footer">
      <p>Desenvolvido por <strong>Lucas Kluska Donini</strong></p>
    </footer>
  </div>
);
}

export default App;
