import React, { Component,Fragment } from 'react';
import {
    BrowserRouter as Router,
    Routes,
    Route,
  } from "react-router-dom";
import Navbar from './layout/Navbar';
import Header from './layout/Header';
import Stopwatch from './Stopwatch';
import Dashboard from './Dashboard';

export default class HomeRoutes extends Component {
  render() {
    return (
      <div>
        <Router>
          <Fragment>
          <Navbar/>
            <main className="main-content position-relative max-height-vh-100 h-100 border-radius-lg ">
            
            
              <Header />
              <div className="container">

              </div>
            </main>
          </Fragment>
      </Router>
      </div>
    )
  }
}
