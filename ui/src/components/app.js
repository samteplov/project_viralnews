import React, {Component} from 'react'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { NavBar } from './navbar.js';
import { Api } from '../api.js';
import { Ml } from '../ml.js';
import { About } from '../about.js';

class App extends Component{
    constructor(){
        super();

    }
    render() {
    	return (
        <React.Fragment>
          <Router>
            <NavBar />
              <Switch>
                <Route exact path="/api" component={Api} />
                <Route exact path="/ml" component={Ml} />
                <Route exact path="/about" component={About} />
              </Switch>
          </Router>
        </React.Fragment>
    		);
    }
}

export default App;
