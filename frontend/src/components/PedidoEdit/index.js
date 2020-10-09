import React from "react";
import { Edit, SimpleForm, TextInput, DateInput } from "react-admin";

const PedidoEdit = props => {
  return (
    <Edit title="Editar cliente" {...props}>
      <SimpleForm>
        <TextInput source="cliente_id" />
        <TextInput source="status" />
        <TextInput source="valor" />
      </SimpleForm>
    </Edit>
  );
};

export default PedidoEdit;
