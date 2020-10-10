import React from "react";
import { Layout } from "react-admin";
import MyAppBar from "./MyAppBar.jsx";

const MyLayout = props => <Layout {...props} appBar={MyAppBar} />;

export default MyLayout;
