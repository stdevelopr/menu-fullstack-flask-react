import React, { useState, useEffect } from "react";
import ReactApexChart from "react-apexcharts";

const statusMock = ["aberto", "aberto", "em andamento", "concluido", "null"];

const chartOptions = {
  chart: {
    type: "donut"
  },
  title: {
    text: "Pedidos por status",
    align: "top"
  },
  noData: {
    text: "Sem pedidos..."
  },
  plotOptions: {
    pie: {
      donut: {
        labels: {
          show: true,
          name: {
            show: true
          },
          total: {
            show: true,
            label: "Total",
            color: "black"
          }
        }
      }
    }
  },
  labels: [],
  legend: {
    position: "bottom"
  }
};

// counts the number of different status
const statusReducer = (accumulator, current_value) => {
  if (current_value in accumulator) {
    accumulator[current_value] += 1;
  } else {
    accumulator[current_value] = 1;
  }
  return accumulator;
};

const PieChart = ({ pedidos }) => {
  const [series, setSeries] = useState([]);
  const [options, setOptions] = useState(chartOptions);

  useEffect(() => {
    // count the number of status and set the options labels state
    let optionsCopy = JSON.parse(JSON.stringify(chartOptions));
    if (pedidos.length > 0) {
      let dictRes = pedidos.map(item => item.status).reduce(statusReducer, {});
      setSeries(Object.values(dictRes));
      optionsCopy.labels = Object.keys(dictRes);
      setOptions(optionsCopy);
    }
  }, [pedidos]);

  return (
    <div id="chart">
      <ReactApexChart options={options} series={series} type="donut" />
    </div>
  );
};

export default PieChart;
