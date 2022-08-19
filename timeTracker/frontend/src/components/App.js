import React, { Component,Fragment } from 'react';
import Stopwatch from "./Stopwatch";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import Dashboard from './Dashboard';
import Navbar from './layout/Navbar';
import Header from './layout/Header';




export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (<div>
              <Router>
                <Fragment>
                  <Navbar/>

                  <main className="main-content position-relative max-height-vh-100 h-100 border-radius-lg ">
                    <Header />
                    <div className="container">
                      <Routes>
                        <Route exact path="/clock" element={<Stopwatch/>}/>
                        <Route exact path="/dashboard" element={<Dashboard/>}/>
                      </Routes>
                    </div>
                  </main>
                </Fragment>
              </Router>
            </div>
       
    
    );
  }
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);