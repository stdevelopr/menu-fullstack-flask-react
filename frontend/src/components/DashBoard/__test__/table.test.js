import React from "react";
import ReactDOM from "react-dom";
import DashTable from "../DashTable";
import renderer from "react-test-renderer";

const clientes = [
  {
    id: 1,
    primeiro_nome: "test_client"
  }
];

const pedidos = [
  {
    id: 1,
    cliente_id: 1,
    valor: 100,
    status: null,
    data: null
  }
];

test("renderiza corretamente", () => {
  const tree = renderer
    .create(<DashTable clientes={clientes} pedidos={pedidos} />)
    .toJSON();
  expect(tree).toMatchSnapshot();
});
