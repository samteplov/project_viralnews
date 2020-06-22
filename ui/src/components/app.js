import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import NavBar from './navbar.js';
import Home from '../home.js';
import Api from '../api.js';
import Ml from '../ml.js';
import About from '../about.js';
import Dashboard from '../dashboard.js';
import '../css/app.css'


class App extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
        <React.Fragment id="container">
          <Router>
            <NavBar />
              <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/index" component={Home} />
                <Route path="/api" component={Api} />
                <Route path="/ml" component={Ml} />
                <Route path="/about" component={About} />
                <Route path="/dashboard" component={Dashboard} />
              </Switch>
          </Router>
        </React.Fragment>
    );
  }
}

export default App;