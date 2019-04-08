import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './router'
import "antd/dist/antd.css";

import CustromLayout from './containers/Layout';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <CustromLayout>
            <BaseRouter />
          </CustromLayout>
        </Router>
      </div>
    );
  }
}

export default App;
