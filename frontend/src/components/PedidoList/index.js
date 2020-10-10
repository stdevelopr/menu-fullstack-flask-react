import React from "react";
import {
  List,
  Datagrid,
  DateField,
  TextField,
  EditButton,
  DeleteButton,
  ReferenceField
} from "react-admin";

const PedidoList = props => {
  return (
    <List {...props}>
      <Datagrid>
        <TextField source="id" />
        <ReferenceField source="cliente_id" reference="clientes">
          <TextField label="Nome" source="primeiro_nome" />
        </ReferenceField>
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
