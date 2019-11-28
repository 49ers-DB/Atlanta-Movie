import React, {Component} from "react";
import customerRegister from "../../actions/registerCustomer";
import APIClient from "../../apiClient.js"



export default class CustomerRegistration extends Component {

    state = {
        firstname: '',
        lastname: '',
        username: '',
        password: '',
        password2: '',
        creditCard: '',
        creditCardsList:[],
    }



    handleChange = event => {
        this.setState({[event.target.name]: event.target.value});
    }

    register() {
        //Checking to make sure all of the fields are filled out correctly
        if(this.state.firstname === '' || 
        this.state.lastname === '' || 
        this.state.username === '' || 
        this.state.password === '' || 
        this.state.creditCard === '') {
            window.alert("Please fill out all of the fields");
        } else if(this.state.firstname.length > 128) {
            window.alert("First name is too long");
        } else if(this.state.lastname.length > 128) {
            window.alert("Last name is too long");
        } else if(this.state.username.length > 128) {
            window.alert("username is too long");
        } else if(this.state.password.length > 128) {
            window.alert("Password is too long");
        } else if(this.state.password.length < 8) {
            window.alert("Password must be at least 8 characters long");
        } else if(this.state.creditCard.length < 16) {
            window.alert("Invalid credit card");
        } else if(this.state.password !== this.state.password2) {
            window.alert("Passwords do not match");
        } else {
            //Credit card validation
            var creditString = this.state.creditCard;
            var count = 0;
            var cards = []
            while(creditString && count < 5) {
                //omit spaces and commas between credit card numbers
                while(creditString[0] === "," || creditString[0] === " ") {
                    creditString = creditString.substring(1);
                }
                var cardNumber = creditString.substring(0,16);
                if(cardNumber.length < 16) {
                    window.alert("Invalid Credit Card Format")
                }

                //if the credit card has any characters besides just numbers
                if(cardNumber.match(/^[0-9]+$/) == null) {
                    window.alert("Invalid credit card format");
                    return;
                }
                if(cards.indexOf(cardNumber) !== -1) {
                    window.alert("Duplicate Credit Cards Found");
                    return;
                }
                cards[count] = cardNumber;
                count++;

                //if the user tries to add more than 5 credit cards
                if(count > 5) {
                    window.alert("You can only add up to 5 credit cards");
                    return;
                }

                //new credit card string omitting the previous credit card
                creditString = creditString.substring(16);
            }
            this.setState(
                {creditCardsList: cards},
                function() {
                    // var registration = customerRegister1(this.state)
                    // console.log(registration)
                    var apiClient = new APIClient("")
                    apiClient.registerCustomer(this.state).then( resp => {
                        console.log(resp)
                        if(resp[1] !== 200) {
                            if(resp[1] === 402) {
                                window.alert("Credit Card Invalid")
                            }
                        } else if(resp[1] === 200) {
                            window.alert("Customer Registered")
                            window.location.replace("/");
                        }
                });
            });

            // var apiClient = new APIClient("")
            // apiClient.registerCustomer(this.state).then( resp => {

            // });

        }
    }
    

    render() {
        return(
            <div className="main">
                <div className="card registrationCard">
                    <h2 className="card-header">Cutomer Registration</h2>
                    <div className="card-body">
                        <div className="nameRegister row">
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        First Name
                                    </label>
                                </div>
                                <input type="text" name="firstname" onChange={this.handleChange} className="form-control" id="firstname"/>
                            </div>
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        Last Name
                                    </label>
                                </div>
                                <input type="text" name="lastname" onChange={this.handleChange} className="form-control" id="lastname"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-12">
                                <div className="col-2">
                                    <label className="registerLabel">
                                        username
                                    </label>
                                </div>
                                
                                <input type="username" name="username" onChange={this.handleChange}  className="form-control" id="username"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <div className="col-4">
                                    <label className="registerLabel">
                                        Password
                                    </label>
                                </div>
                                <input type="password" name="password" onChange={this.handleChange}  className="form-control" id="password"/>
                            </div>
                            <div className="col-6">
                                <div className="col-6">
                                    <label className="registerLabel">
                                        Confirm Password
                                    </label>
                                </div>
                                <input type="password" name="password2" onChange={this.handleChange}  className="form-control" id="password2"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-12">
                                <div className="col-3">
                                    <label className="registerLabel">
                                        Credit Cards
                                    </label>
                                </div>
                                    <input type="text" name="creditCard" onChange={this.handleChange} className="form-control" id="text" placeholder='Separate each cards with a ","'/>
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
