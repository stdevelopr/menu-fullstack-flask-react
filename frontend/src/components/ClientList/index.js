import React from "react";
import {
  List,
  Datagrid,
  TextField,
  EditButton,
  DeleteButton
} from "react-admin";

const ClientList = props => {
  return (
    <List {...props}>
      <Datagrid>
        <TextField source="id" />
        <TextField source="primeiro_nome" />
        <TextField source="ultimo_nome" />
        <TextField source="email" />
        <EditButton basePath="/clientes" />
        <DeleteButton basePath="/clientes" />
      </Datagrid>
    </List>
  );
};

export default ClientList;
