import React, {Component} from "react";
import "./UserRegistration.css"


export default class UserRegistration extends Component {

    state = {
        firstName: '',
        lastName: '',
        Username: '',
        password: '',
        password2: '',
    }

    //check if user already exists


    handleChange = event => {
        this.setState({[event.target.name]: event.target.value});
    }
    register() {
        //Checking to make sure all of the fields are filled out correctly
        console.log(this.state);
        if(this.state.firstName === '' || 
        this.state.lastname === '' || 
        this.state.Username === '' || 
        this.state.password === '') {
            window.alert("Please fill out all of the fields");
        } else if(this.state.firstName.length > 128) {
            window.alert("First name is too long");
        } else if(this.state.lastName.length > 128) {
            window.alert("Last name is too long");
        } else if(this.state.Username.length > 128) {
            window.alert("Username is too long");
        } else if(this.state.password.length > 128) {
            window.alert("Password is too long");
        } else if(this.state.password.length < 8) {
            window.alert("Password must be at least 8 characters long");
        } else if(this.state.password !== this.state.password2) {
            window.alert("Passwords do not match");
        } else {
            
            //post method
        }
    }
    
    render() {
        return(
            <div className="main">
                <div className="card registrationCard">
                    <h2 className="card-header">User Registration</h2>
                    <div className="card-body">
                        <div className="nameRegister row">
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        First Name
                                    </label>
                                </div>
                                <input type="text" name="firstName" onChange={this.handleChange} className="form-control" id="firstName"/>
                            </div>
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        Last Name
                                    </label>
                                </div>
                                <input type="text" name="lastName" onChange={this.handleChange} className="form-control" id="lastName"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-12">
                                <div className="col-2">
                                    <label className="registerLabel">
                                        Username
                                    </label>
                                </div>
                                
                                <input type="Username" name="Username" onChange={this.handleChange} className="form-control" id="Username"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        Password
                                    </label>
                                </div>
                                <input type="text" name="password" onChange={this.handleChange} className="form-control" id="password"/>
                            </div>
                            <div className="col-6">
                                <div className="col-6">
                                    <label className="registerLabel">
                                        Confirm Password
                                    </label>
                                </div>
                                <input type="text" name="password2" onChange={this.handleChange} className="form-control" id="password2"/>
                            </div>
                        </div>
                        <div className="row buttonRows">
                            <div className="col-6">
                                <div className="LoginButton">
                                    <a type="back" className="btn btn-primary" href="/Register-Option">Back</a>
                                </div>
                            </div>
                            <div className="col-6">
                                <div className="RegisterButton">
                                    <div className="btn btn-primary" onClick={() => this.register()}>Register</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}