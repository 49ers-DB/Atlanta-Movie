import React, {Component} from 'react';
import './App.css';
import {BrowserRouter as Router, Route} from "react-router-dom";
import NavBar from './Components/NavBar';
import Login from './Components/Login'
import 'bootstrap/dist/css/bootstrap.min.css';
import RegisterOption from './Components/Register/RegisterOption';
import CustomerRegistration from './Components/Register/CustomerRegistration.js';
import ManagerRegistration from './Components/Register/ManagerRegistration';
import ManagerCustomerRegistration from './Components/Register/ManagerCustomerRegistration';
import UserRegistration from './Components/Register/UserRegistration';


class App extends Component {

  

  render() {

    return (
      <div className="App">
        <Router>
          
          <NavBar />
          <Route exact path="/" component={Login} />
          <Route exact path="/Register-Option" component={RegisterOption}/>
          <Route exact path="/Customer-Registration" component={CustomerRegistration}/>
          <Route exact path="/Manager-Registration" component={ManagerRegistration}/>
          <Route exact path="/Manager-Customer-Registration" component={ManagerCustomerRegistration}/>
          <Route exact path="/User-Registration" component={UserRegistration}/>

        </Router>
      </div>
    );
  }
  
}

export default App;