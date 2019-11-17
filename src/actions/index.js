import React from 'react'
import Button from '@material-ui/core/Button';
import { Redirect } from 'react-router-dom'
import userLoginFetch from './actions.js'
import userLogin from './actions.js'

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
        <div style={{height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
          <form onSubmit={this.login}>
            <h1>Login</h1>
            <label>Username</label>
            <input
              name='username'
              placeholder='Username'
              value={this.state.username}
              onChange={this.handleChange}
              /><br/>

            <label>Password</label>
            <input
              type='password'
              name='password'
              placeholder='Password'
              value={this.state.password}
              onChange={this.handleChange}
              /><br/>

            <Button type='submit' variant="contained" color="primary" onClick={this.login}>Login</Button>
            <Button variant="contained" color="primary" onClick={this.login}>Register</Button>
            
          </form>
        </div>
      )
    }
  }
 }

//  const mapDispatchToProps = dispatch => ({
//   userLoginFetch: userInfo => dispatch(userLoginFetch(userInfo))
// })
 
 export default (Login);