import React from "react";
import { Admin, Resource } from "react-admin";
import restProvider from "ra-data-simple-rest";
import DashBoard from "./components/DashBoard";
import ClientList from "./components/ClientList";
import ClientCreate from "./components/ClientCreate";
import ClientEdit from "./components/ClientEdit";
import PedidoList from "./components/PedidoList";
import PedidoCreate from "./components/PedidoCreate";
import PedidoEdit from "./components/PedidoEdit";
import PostIcon from "@material-ui/icons/Book";
import UserIcon from "@material-ui/icons/Group";

const App = () => (
  <Admin
    dashboard={DashBoard}
    dataProvider={restProvider("http://localhost:5000")}
  >
    <Resource
      name="clientes"
      list={ClientList}
      create={ClientCreate}
      edit={ClientEdit}
      icon={UserIcon}
    />
    <Resource
      name="pedidos"
      list={PedidoList}
      create={PedidoCreate}
      edit={PedidoEdit}
      icon={PostIcon}
    />
  </Admin>
);

export default App;
