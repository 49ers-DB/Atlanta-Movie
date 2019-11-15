import React, {Component} from "react";
import "./UserRegistration.css"


export default class UserRegistration extends Component {

    state = {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        password2: '',
    }

    //check if user already exists


    setFirstName(typedFirstName) {
        this.setState({
            firstName: typedFirstName
        });
    }
    setLastName(typedLastName) {
        this.setState({
            lastName: typedLastName
        });
    }
    setEmail(typedEmail) {
        this.setState({
            email: typedEmail
        });
    }
    setPassword(typedPassword) {
        this.setState({
            password: typedPassword
        });
    }
    setPassword2(typedPassword) {
        this.setState({
            password2: typedPassword
        });
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
                                <input type="text" onChange={e => this.setFirstName(e.target.value) } className="form-control" id="firstName"/>
                            </div>
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        Last Name
                                    </label>
                                </div>
                                <input type="text" onChange={e => this.setLastName(e.target.value) } className="form-control" id="lastName"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-12">
                                <div className="col-2">
                                    <label className="registerLabel">
                                        Email
                                    </label>
                                </div>
                                
                                <input type="email" onChange={e => this.setEmail(e.target.value) } className="form-control" id="email"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        Password
                                    </label>
                                </div>
                                <input type="text" onChange={e => this.setPassword(e.target.value) } className="form-control" id="password"/>
                            </div>
                            <div className="col-6">
                                <div className="col-6">
                                    <label className="registerLabel">
                                        Confirm Password
                                    </label>
                                </div>
                                <input type="text" onChange={e => this.setPassword2(e.target.value) } className="form-control" id="password2"/>
                            </div>
                        </div>
                        <div className="row buttonRows">
                            <div className="col-6">
                                <div className="LoginButton">
                                    <a type="back" className="btn btn-primary" href="/">Back</a>
                                </div>
                            </div>
                            <div className="col-6">
                                <div className="RegisterButton">
                                    <a type="register" className="btn btn-primary" href="/">Register</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}