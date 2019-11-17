import React, {Component} from "react";
// import "./ManagerRegistration.css";
import Select from "react-select";

var companies = [];
const stateOptions = [
    {value: "AL", label: "AL"},
    {value: "AK", label: "AK"},
    {value: "AZ", label: "AZ"},
    {value: "AR", label: "AR"},
    {value: "CA", label: "CA"},
    {value: "CO", label: "CO"},
    {value: "CT", label: "CT"},
    {value: "DE", label: "DE"},
    {value: "FL", label: "FL"},
    {value: "GA", label: "GA"},
    {value: "HI", label: "HI"},
    {value: "ID", label: "ID"},
    {value: "IL", label: "IL"},
    {value: "IN", label: "IN"},
    {value: "IA", label: "IA"},
    {value: "KS", label: "KS"},
    {value: "KY", label: "KY"},
    {value: "LA", label: "LA"},
    {value: "ME", label: "ME"},
    {value: "MD", label: "MD"},
    {value: "MA", label: "MA"},
    {value: "MI", label: "MI"},
    {value: "MN", label: "MN"},
    {value: "MS", label: "MS"},
    {value: "MO", label: "MO"},
    {value: "MT", label: "MT"},
    {value: "NE", label: "NE"},
    {value: "NV", label: "NV"},
    {value: "NH", label: "NH"},
    {value: "NJ", label: "NJ"},
    {value: "NM", label: "NM"},
    {value: "NY", label: "NY"},
    {value: "NC", label: "NC"},
    {value: "ND", label: "ND"},
    {value: "OH", label: "OH"},
    {value: "OK", label: "OK"},
    {value: "OR", label: "OR"},
    {value: "PA", label: "PA"},
    {value: "RI", label: "RI"},
    {value: "SC", label: "SC"},
    {value: "SD", label: "SD"},
    {value: "TN", label: "TN"},
    {value: "TX", label: "TX"},
    {value: "UT", label: "UT"},
    {value: "VT", label: "VT"},
    {value: "VA", label: "VA"},
    {value: "WA", label: "WA"},
    {value: "WV", label: "WV"},
    {value: "WI", label: "WI"},
    {value: "WY", label: "WY"},
]

export default class ManagerRegistration extends Component {

    state = {
        firstName: '',
        lastName: '',
        Username: '',
        password: '',
        password2: '',
        address: '',
        zipCode: '',
        selectedCompany: {value: "None", label: "None"},
        selectedState: null,
    }
    
    getCompanies() {
        //fetch list of companies
        //dummy data
        companies = [
            {value: "None", label: "None"},
            {value: "AMC", label: "AMC"},
            {value: "Regal", label: "Regal"},
            {value: "Carmike's", label: "Carmike's"}
        ]
        return companies;
    }

    setCompany = selectedCompany => {
        this.setState({selectedCompany})
    }
    setSelectedState = selectedState => {
        this.setState({selectedState})
    }

    handleChange = event => {
        this.setState({[event.target.name]: event.target.value});
    }
    register() {
        //Checking to make sure all of the fields are filled out correctly
        console.log(this.state);
        if(this.state.firstName === '' || 
        this.state.lastname === '' || 
        this.state.Username === '' || 
        this.state.password === '' ||
        this.state.address === '' ||
        this.state.zipCode === '') {
            window.alert("Please fill out all of the fields");
        } else if(this.state.firstName.length > 128) {
            window.alert("First name is too long");
        } else if(this.state.lastName.length > 128) {
            window.alert("Last name is too long");
        } else if(this.state.Username.length > 128) {
            window.alert("Username is too long");
        } else if(this.state.password.length > 128) {
            window.alert("Password is too long");
        } else if(this.state.address.length > 128) {
            window.alert("Address is too long");
        } else if(this.state.zipCode.length !== 5) {
            window.alert("Zip Code must be 5 characters long");
        } else if(this.state.zipCode.match(/^[0-9]+$/) == null) {
            window.alert("Zip Code must be only numbers");
        } else if(this.state.password.length < 8) {
            window.alert("Password must be at least 8 characters long");
        } else if(this.state.selectedCompany.value === "None") {
            window.alert("Choose a company");
        } else if(this.state.setSelectedState.value === "None") {
            window.alert("Choose a company");
        } else if(this.state.password !== this.state.password2) {
            window.alert("Passwords do not match");
        } else {
            
            //post method
        }
    }
    
    render() {
        const { selectedCompany,
                selectedState
             } = this.state;
        return(
            <div className="main">
                <div className="card registrationCard">
                    <h2 className="card-header">Manager Registration</h2>
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
                            <div className="col-6">
                                <div className="col-2">
                                    <label className="registerLabel">
                                        Username
                                    </label>
                                </div>
                                <input type="Username" name="Username" onChange={this.handleChange} className="form-control" id="Username"/>
                            </div>
                            <div className="col-6">
                                <div className="col-2">
                                    <label className="registerLabel">
                                        Company
                                    </label>
                                </div>
                                <Select
                                value={selectedCompany}
                                onChange={this.setCompany}
                                options={this.getCompanies()}
                                placeholder="None"
                                />
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
                        <div className="row">
                            <div className="col-12">
                                <div className="col-3">
                                    <label className="registerLabel">
                                        Street Address
                                    </label>
                                </div>
                                <input type="text" name="address" onChange={this.handleChange} className="form-control" id="address"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-5">
                                <div className="col-6">
                                    <label className="registerLabel">
                                        City
                                    </label>
                                </div>
                                <input type="text" name="city" onChange={this.handleChange} className="form-control" id="city"/>
                            </div>
                            <div className="col-3">
                                <div className="col-6">
                                    <label className="registerLabel">
                                        State
                                    </label>
                                </div>
                                <Select
                                    value={selectedState}
                                    onChange={this.setSelectedState}
                                    options={stateOptions}
                                    placeholder="Select"
                                    />
                            </div>
                            <div className="col-4">
                                <div className="col-6">
                                    <label className="registerLabel">
                                        Zip Code
                                    </label>
                                </div>
                                <input type="text" name="zipCode" onChange={this.handleChange} className="form-control" id="zipCode"/>
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