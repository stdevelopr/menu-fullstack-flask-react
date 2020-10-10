import React from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";

export default function DashTable({ pedidos, clientes }) {
  const getClient = client_id => {
    let client = clientes.find(cliente => cliente.id == client_id)
      .primeiro_nome;
    return client;
  };

  return (
    <TableContainer component={Paper}>
      <div style={{ textAlign: "center" }}>
        <b>Últimos pedidos</b>
      </div>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>
              <b>Cliente</b>
            </TableCell>
            <TableCell align="right">
              <b>Valor</b>
            </TableCell>
            <TableCell align="right">
              <b>Status</b>
            </TableCell>
            <TableCell align="right">
              <b>Data</b>
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {pedidos
            .reverse()
            .slice(0, 5)
            .map(pedido => (
              <TableRow key={pedido.id}>
                <TableCell component="th" scope="row">
                  {getClient(pedido.cliente_id)}
                </TableCell>
                <TableCell align="right">{pedido.valor}</TableCell>
                <TableCell align="right">{pedido.status}</TableCell>
                <TableCell align="right">
                  {new Date(pedido.data).toLocaleDateString("pt-BR")}
                </TableCell>
              </TableRow>
            ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
