import React, { Component,Fragment } from 'react';
import GenericHeader from './layout/GenericHeader';
import Login from './account/Login';
import Register from './Register';
import {
    BrowserRouter as Router,
    Routes,
    Route,
  } from "react-router-dom";

export default class AuthRoutes extends Component {
  render() {
    return (
     
        <div>
        <Router>
          <Fragment>
            <GenericHeader/>
              <div className="container">
                <Routes>
                  <Route exact path="/login" element={<Login/>}/>
                  <Route exact path="/register" element={<Register/>}/>
                  
                </Routes>
              </div>
 
          </Fragment>
      </Router>
      </div>
  
    )
  }
}
