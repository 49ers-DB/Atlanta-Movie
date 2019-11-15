import React from 'react';
import { Redirect } from 'react-router-dom';
import userLoginFetch from '../actions/actions.js';
import './Login.css';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      authenticated: null,
      username: "",
      password: "",
    };
    // this.checkAuthentication = this.checkAuthentication.bind(this);
    this.login = this.login.bind(this);
  }

  handleChange = event => {
    this.setState({[event.target.name]: event.target.value});
  }

  login = event => {
    console.log("Loging in with username: %s, password %s", this.state.username, this.state.password)
    event.preventDefault()
    var token = userLoginFetch(this.state)
    console.log(token)

  }
 
  // async checkAuthentication() {
  //   // const authenticated = await this.props.auth.isAuthenticated();
  //   // if (authenticated !== this.state.authenticated) {
  //   //   this.setState({ authenticated });
  //   // }
  // }
 
  // async componentDidMount() {
  //   this.checkAuthentication()
  // }
 
  // async login(e) {
  //   this.props.login('/home');
  // }
 
  render() {
    if (this.state.authenticated) {
      return <Redirect to='/home' />
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
                                    <div className="btn btn-primary" onClick={this.login}>Login</div>
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

//  const mapDispatchToProps = dispatch => ({
//   userLoginFetch: userInfo => dispatch(userLoginFetch(userInfo))
// })
 
 export default (Login);