import React, { Component,Fragment } from 'react';
import Stopwatch from "./Stopwatch";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import HomeRoutes from './HomeRoutes';
import AuthRoutes from './AuthRoutes';




export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (<div>
      <Router>
          <Fragment>
          
          <Routes>
            <Route exact path="/a" element={<AuthRoutes/>}/>
            <Route exact path="/acc" element={<HomeRoutes/>}/>
                  
          </Routes>
          
          </Fragment>
      </Router>
    </div>
       
    
    );
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);