import React, { useState, useEffect } from "react";
import ReactApexChart from "react-apexcharts";

//// Essa variável pode ser usada para testar o gráfico, basta ser substituida por pedidos dentro de useEffect
// const mockPedidos = [
//   { data: "2020-10-09T00:00:00.0000", valor: 100 },
//   { data: "2020-10-10T00:00:00.0000", valor: 100 },
//   { data: "2020-10-10T00:00:00.0000", valor: 100 },
//   { data: "2020-10-11T00:00:00.0000", valor: 100 },
//   { data: "2020-10-14T00:00:00.0000", valor: 500 }
// ];

const options = {
  chart: {
    type: "line",
    zoom: {
      enabled: false
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    curve: "straight",
    width: 3,
    dashArray: 3
  },
  markers: {
    size: 5
  },
  title: {
    text: "Valor acumulado por dia",
    align: "left"
  },
  grid: {
    row: {
      colors: ["#f3f3f3", "transparent"],
      opacity: 0.5
    }
  },
  xaxis: {
    type: "datetime"
  }
};

// this function returns the accumulative sum for each date
const dateValueReducer = (accumulator, current_value) => {
  let dateRef = new Date(current_value.data).toLocaleDateString();
  if (dateRef in accumulator) {
    accumulator[dateRef] += current_value.valor;
  } else {
    accumulator[dateRef] = current_value.valor;
  }
  return accumulator;
};

const LineChart = ({ pedidos }) => {
  const [series, setSeries] = useState([
    {
      name: "Valor",
      data: []
    }
  ]);

  useEffect(() => {
    // when there are orders calculate the cumulative sum and set to the data in the state series
    let seriesCopy = JSON.parse(JSON.stringify(series));
    if (pedidos.length > 0) {
      let dictRes = pedidos.reduce(dateValueReducer, {});

      let pedidosSum = Object.keys(dictRes).map(item => {
        return { x: item, y: dictRes[item] };
      });
      seriesCopy[0].data = pedidosSum;
      setSeries(seriesCopy);
    }
  }, [pedidos]);

  return <ReactApexChart options={options} series={series} type="line" />;
};

export default LineChart;
