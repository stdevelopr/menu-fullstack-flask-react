import React from "react";
import { Edit, SimpleForm, TextInput, DateInput } from "react-admin";

const ClientEdit = props => {
  return (
    <Edit title="Editar cliente" {...props}>
      <SimpleForm>
        <TextInput source="primeiro_nome" />
        <TextInput source="ultimo_nome" />
        <TextInput source="email" />
      </SimpleForm>
    </Edit>
  );
};

export default ClientEdit;
