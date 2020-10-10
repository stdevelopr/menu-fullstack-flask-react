import React from "react";
import { Create, SimpleForm, TextInput, DateInput } from "react-admin";

const PedidoCreate = props => {
  return (
    <Create title="Criar Pedido" {...props}>
      <SimpleForm redirect="list">
        <TextInput label="Cliente ID" source="cliente_id" />
        <TextInput source="status" />
        <TextInput source="valor" />
      </SimpleForm>
    </Create>
  );
};

export default PedidoCreate;
