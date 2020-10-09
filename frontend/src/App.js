import React from "react";
import { Admin, Resource } from "react-admin";
import restProvider from "ra-data-simple-rest";
import ClientList from "./components/ClientList";
import ClientCreate from "./components/ClientCreate";
import ClientEdit from "./components/ClientEdit";

const App = () => (
  <Admin dataProvider={restProvider("http://localhost:5000")}>
    <Resource
      name="clientes"
      list={ClientList}
      create={ClientCreate}
      edit={ClientEdit}
    />
  </Admin>
);

export default App;
