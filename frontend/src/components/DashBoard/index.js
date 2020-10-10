import React, { useState, useEffect } from "react";
import { Card, CardContent, CardHeader } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import DashTable from "./DashTable.jsx";
import LineChart from "./LineChart.jsx";
import PieChart from "./PieChart.jsx";

// count the total number of orders
const countTotal = pedidos => {
  return pedidos
    .map(item => item.valor)
    .reduce((accumulator, currentValue) => accumulator + currentValue, 0);
};

export default () => {
  const [clientes, setClientes] = useState([]);
  const [pedidos, setPedidos] = useState([]);

  useEffect(() => {
    Promise.all([
      fetch("http://localhost:5000/clientes"),
      fetch("http://localhost:5000/pedidos")
    ])
      .then(function(responses) {
        // Get a JSON object from each of the responses
        return Promise.all(
          responses.map(function(response) {
            return response.json();
          })
        );
      })
      .then(function(data) {
        setClientes(data[0]);
        setPedidos(data[1]);
      })
      .catch(function(error) {
        console.log(error);
      });
  }, []);

  return (
    <Card>
      <CardHeader title="DashBoard" />
      <CardContent>
        <Grid container spacing={3}>
          <Grid item xs={12} style={{ backgroundColor: "lavender" }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-evenly"
              }}
            >
              <div>
                <b>Total de Clientes:</b> {clientes.length}
              </div>
              <div>
                <b>Valor em Pedidos:</b> {countTotal(pedidos)}
              </div>
            </div>
          </Grid>
          <Grid item xs={12} sm={5}>
            <PieChart pedidos={pedidos} />
          </Grid>
          <Grid item xs={12} sm={7}>
            <LineChart pedidos={pedidos} />
          </Grid>
          <Grid item xs={12}>
            <DashTable pedidos={pedidos} clientes={clientes} />
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};
