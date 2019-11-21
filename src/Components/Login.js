import React from 'react';
import { Redirect } from 'react-router-dom';
import userLogin from '../actions/login.js';
import './Login.css';
import apiClient from '../App.js';

import APIClient from '../apiClient.js';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      authenticated: this.props.authenticated,
      username: "",
      password: "",
    };
    // this.checkAuthentication = this.checkAuthentication.bind(this);
    this.login = this.login.bind(this);
  }

  handleAPIClientChange(client) {
    this.props.handleAPIClientChange(client);
  }

  handleChange = event => {
    this.setState({[event.target.name]: event.target.value});
  }

  login = event => {
    if(this.state.username === '' || this.state.password === '') {
        window.alert("Please enter username and password");
    } else {
        console.log("Logging in with username: %s, password %s", this.state.username, this.state.password)
        event.preventDefault();
        var tokenPromise = userLogin(this.state);
        tokenPromise.then(resp => resp.json())
        .then(data => {
          if (data.message) {
            // Here you should have logic to handle invalid login credentials.
            // This assumes your Rails API will return a JSON object with a key of
            // 'message' if there is an error
            console.error("Bad login parameters")
            
          } else {
            // localStorage.setItem("token", data.jwt)
            // dispatch(loginUser(data.user))
            console.log("logged in")
            return data;
          }
        })
        
        // if (token !== null) {
        //   console.log(token);
        //   this.setState({authenticated: true});
        
        //   this.handleAPIClientChange(new APIClient(token));
        // }
        
    }
  }
 
  render() {
    if (this.state.authenticated) {
      return <Redirect to='/menu' />
    } else {
      return (
            <div className="main">
                <div className="card loginCard">
                    <h2 className="card-header">Atlanta Movie Login</h2>
                    <div className="card-body">
                        <form onSubmit={this.login}>
                            <label className="col-4">Username</label>
                            <input
                            className="col-8"
                            name='username'
                            placeholder='Username'
                            value={this.state.username}
                            onChange={this.handleChange}
                            /><br/>

                            <label className="col-4">Password</label>
                            <input
                            className="col-8"
                            type='password'
                            name='password'
                            placeholder='Password'
                            value={this.state.password}
                            onChange={this.handleChange}
                            /><br/>
                            <div className="row buttonRows">
                                <div className="col-6">
                                    <button className="btn btn-primary" type="submit">Login</button>
                                </div>
                                <div className="col-6">
                                    <a className="btn btn-primary" href="/Register-Option">Register</a>
                                </div>
                            </div>
                            
                        </form>
                    </div>
                </div>
            </div>
      )
    }
  }
 }
 
 export default (Login);