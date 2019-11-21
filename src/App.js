import React, {Component} from 'react';
import './App.css';
import {BrowserRouter as Router, Route} from "react-router-dom";
import NavBar from './Components/NavBar';
import Login from './Components/Login'
import 'bootstrap/dist/css/bootstrap.min.css';
import APIClient from "./apiClient.js"
import RegisterOption from './Components/Register/RegisterOption';
import CustomerRegistration from './Components/Register/CustomerRegistration.js';
import ManagerRegistration from './Components/Register/ManagerRegistration';
import ManagerCustomerRegistration from './Components/Register/ManagerCustomerRegistration';
import UserRegistration from './Components/Register/UserRegistration';
import Menu from './Components/Menu/Menu';



class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      authenticated: null
    };
    this.handleAPIClientChange = this.handleAPIClientChange.bind(this)
  }  

  handleAPIClientChange(client) {
    console.log(client)
    client.example(12).then( () => {
      this.setState({
        apiClient: client,
        authenticated: true
      });
    }
      
    );
    
  }

  render() {

    return (
      <div className="App">
        <Router>
          
          <NavBar />
          <Route exact path="/" component={() => <Login handleAPIClientChange={this.handleAPIClientChange} authenticated={this.state.authenticated}/>} />
          <Route exact path="/Register-Option" component={RegisterOption}/>
          <Route exact path="/Customer-Registration" component={CustomerRegistration}/>
          <Route exact path="/Manager-Registration" component={ManagerRegistration}/>
          <Route exact path="/Manager-Customer-Registration" component={ManagerCustomerRegistration}/>
          <Route exact path="/User-Registration" component={UserRegistration}/>
          <Route exact path="/Menu" component={() => <Menu apiClient={this.state.apiClient}/>} />
          {/* <Route exact path="/Manage-User" component={ManageUser} /> */}

        </Router>
      </div>
      
    );
  }
  
}

export default (App);