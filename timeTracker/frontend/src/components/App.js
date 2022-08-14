import React, { Component } from 'react';
import Stopwatch from "./Stopwatch";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Dashboard from './Dashboard';


export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
      
      <Router>
      <Routes>
          <Route exact path="/" element={<Stopwatch/>}/>
          <Route exact path="/dashboard" element={<Dashboard/>}/>

        </Routes>
      </Router>
      </div>
    );
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);