import React from "react";
import {
  List,
  Datagrid,
  DateField,
  TextField,
  EditButton,
  DeleteButton
} from "react-admin";

const PedidoList = props => {
  return (
    <List {...props}>
      <Datagrid>
        <TextField source="id" />
        <TextField label="Cliente ID" source="cliente_id" />
        <TextField source="status" />
        <DateField source="data" locales="pt-BR" />
        <TextField source="valor" />
        <EditButton basePath="/pedidos" />
        <DeleteButton basePath="/pedidos" />
      </Datagrid>
    </List>
  );
};

export default PedidoList;
