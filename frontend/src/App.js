import React from "react";
import { Admin, Resource } from "react-admin";
import restProvider from "ra-data-simple-rest";
import ClientList from "./components/ClientList";

const App = () => (
  <Admin dataProvider={restProvider("http://localhost:5000")}>
    <Resource name="clientes" list={ClientList} />
  </Admin>
);

export default App;
