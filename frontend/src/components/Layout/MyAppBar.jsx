import * as React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import RefreshIcon from "@material-ui/icons/Refresh";
import { makeStyles } from "@material-ui/core/styles";
import { useDispatch } from "react-redux";
import logo from "./logo.png";

const useStyles = makeStyles(theme => ({
  menuStyle: {
    display: "flex",
    justifyContent: "center",
    height: "50px"
  },
  menuButton: {
    marginRight: theme.spacing(1)
  },
  title: {
    flexGrow: 1
  },
  refreshButton: {
    position: "absolute",
    right: "30px"
  }
}));

const MyAppBar = props => {
  const classes = useStyles();
  const dispatch = useDispatch();

  return (
    <div>
      <AppBar {...props} className={classes.menuStyle}>
        <Toolbar>
          <div>
            <img style={{ height: "60px" }} src={logo} />
          </div>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="menu"
            onClick={() => {
              dispatch({
                type: "RA/TOGGLE_SIDEBAR",
                payload: {
                  admin: {
                    ui: {
                      sidebarOpen: false
                    }
                  }
                }
              });
            }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" id="react-admin-title" />
          <IconButton
            className={classes.refreshButton}
            color="inherit"
            onClick={() => location.reload(true)}
          >
            <RefreshIcon />
          </IconButton>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default MyAppBar;
