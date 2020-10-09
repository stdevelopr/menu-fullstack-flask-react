import React from "react";
import {
  List,
  Datagrid,
  TextField,
  DateField,
  EditButton,
  DeleteButton
} from "react-admin";

const ClientList = props => {
  return (
    <List {...props}>
      <Datagrid>
        <TextField source="id" />
        <TextField source="primeiro_nome" />
        <EditButton basePath="/clientes" />
        <DeleteButton basePath="/clientes" />
      </Datagrid>
    </List>
  );
};

export default ClientList;
