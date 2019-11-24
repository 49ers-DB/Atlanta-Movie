import React from 'react';
import { Redirect } from 'react-router-dom';
import userLogin from '../actions/login.js';
import './Login.css';
import APIClient from '../apiClient';
import Alert from './Alert.js'




class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      authenticated: this.props.authenticated,
      username: "",
      password: "",
      showAlert: false,
      title: "",
      message: ""
    };
    // this.checkAuthentication = this.checkAuthentication.bind(this);
    this.login = this.login.bind(this);
  }

  

  handleAlert = (title, message) => {
    this.setState({
      showAlert: true,
      title: title,
      message: message
    });
  }

  handleClose = () => {
    this.setState({showAlert: false});
  };

  handleAPIClientChange(client) {
    this.props.handleAPIClientChange(client);
  }

  handleChange = event => {
    this.setState({[event.target.name]: event.target.value});
  }

  login = event => {
    event.preventDefault();
    if(this.state.username === '' || this.state.password === '') {
        // this.props.alert.error("Please enter username and password");
        this.handleAlert("Login Error", "Please enter username and password")
    } else {
        console.log("Logging in with username: %s, password %s", this.state.username, this.state.password)
        var tokenPromise = userLogin(this.state);

        tokenPromise.then(resp => resp.json())
        .then(data => {
          if (data.message) {
            // Here you should have logic to handle invalid login credentials.
            // This assumes your Rails API will return a JSON object with a key of
            // 'message' if there is an error
            console.error("Bad login parameters")
            this.handleAlert("Could Not Login", "Incorrect username or password");
          } else {
            data = data.data
            
            console.log("got data message", data)
            var token = data.jwt
            console.log(token)
            if (token) {
              localStorage.setItem("accessToken", data.jwt)
              this.setState({authenticated: true});
            }
          }
        })
        
    }
  }
 
  render() {
    if (localStorage.getItem("accessToken") != 'false') {
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
                <Alert show={this.state.showAlert} title={this.state.title} message={this.state.message} handleClose={this.handleClose} ></Alert>
            </div>
      )
    }
  }
 }
 
 export default (Login)

