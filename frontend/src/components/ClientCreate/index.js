import React from "react";
import { Create, SimpleForm, TextInput, DateInput } from "react-admin";

const ClientCreate = props => {
  return (
    <Create title="Criar cliente" {...props}>
      <SimpleForm redirect="list">
        <TextInput source="primeiro_nome" />
        <TextInput source="ultimo_nome" />
        <TextInput source="email" />
      </SimpleForm>
    </Create>
  );
};

export default ClientCreate;
