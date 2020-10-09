import React from "react";
import { Admin, Resource } from "react-admin";
import restProvider from "ra-data-simple-rest";
import ClientList from "./components/ClientList";
import ClientCreate from "./components/ClientCreate";
import ClientEdit from "./components/ClientEdit";
import PedidoList from "./components/PedidoList";
import PedidoCreate from "./components/PedidoCreate";
import PedidoEdit from "./components/PedidoEdit";

const App = () => (
  <Admin dataProvider={restProvider("http://localhost:5000")}>
    <Resource
      name="clientes"
      list={ClientList}
      create={ClientCreate}
      edit={ClientEdit}
    />
    <Resource
      name="pedidos"
      list={PedidoList}
      create={PedidoCreate}
      edit={PedidoEdit}
    />
  </Admin>
);

export default App;
