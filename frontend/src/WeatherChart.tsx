import EChartsReact from "echarts-for-react";

export interface ChartData {
  min_temps: number[];
  max_temps: number[];
  humidities: number[];
  dates: string[];
}

const WeatherChart = ({
  min_temps,
  max_temps,
  humidities,
  dates,
}: ChartData) => {
  const getSeries = (title: string, data: number[], color: string) => {
    return {
      name: title,
      data: data,
      type: "line",
      smooth: true,
      showSymbol: false,
      itemStyle: { color: color },
    };
  };

  const option = {
    title: {
      text: "Variação Climática (ESG Tracker)",
      left: "center",
      textStyle: {
        color: "#eee",
      },
    },
    tooltip: { trigger: "axis" },
    xAxis: {
      type: "category",
      data: dates,
      boundaryGap: false,
      axisLine: {
        lineStyle: {
          color: "#eee",
        },
      },
    },
    yAxis: [
      {
        type: "value",
        name: "Temperatura (°C)",
        min: 0,
        max: 50,
        position: "left",
        axisLine: {
          lineStyle: {
            color: "#eee",
          },
        },
      },
      {
        type: "value",
        name: "Umidade (%)",
        min: 50,
        max: 100,
        position: "right",
        axisLine: {
          lineStyle: {
            color: "#eee",
          },
        },
      },
    ],
    series: [
      getSeries("Mínima (C°)", min_temps, "#00cc88"),
      getSeries("Máxima (C°)", max_temps, "#cc4b00ff"),
      {
        ...getSeries("Umidade (%)", humidities, "rgba(0, 157, 255, 0.4)"),
        yAxisIndex: 1,
        type: "bar",
      },
    ],
    grid: { bottom: "10%", containLabel: true },
    dataZoom: [
      {
        type: "inside",
        start: 0,
        end: 100,
      },
      {
        start: 0,
        end: 100,
      },
    ],
  };

  return (
    <div style={{ width: "100%", height: "100%" }}>
      <EChartsReact
        option={option}
        style={{ height: "100%", width: "100%" }}
        opts={{ renderer: "canvas" }}
      />
    </div>
  );
};

export default WeatherChart;
