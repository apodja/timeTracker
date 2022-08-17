import React, { Component } from 'react';
import Stopwatch from "./Stopwatch";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Dashboard from './Dashboard';
import SignInSide from './SignIn';
import Register from './Register'
import Login from './Login';



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
          <Route exact path="/login" element={<Login/>}/>
          <Route exact path="/register" element={<Register/>}/>
        </Routes>
      </Router>
      </div>
    );
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);