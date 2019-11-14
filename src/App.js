import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom' 

import Login from './Login';

function App() {
  return (
    <Router>
      <Switch>
           <Route exact path="/" component={Login} />
           {/* <Route path="/implicit/callback" component={ImplicitCallback} />
           <SecureRoute path="/home" component={Home} /> */}
      </Switch>
    </Router>
    
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
  );
}

export default App;
