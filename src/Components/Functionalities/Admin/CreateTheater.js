import React, { Component } from 'react'
import APIClient from "../../../apiClient"
import Select from 'react-select'
import stateOptions from "../../../actions/stateOptions"
import getCompanies from "../../../actions/companies"
import managers from "../../../actions/managers"


import "../Functionality.css"

export default class CreateTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      i_thName: "",
      i_comName: null,
      i_thStreet: "",
      i_thCity: "",
      i_thState: null,
      i_thZipcode: "",
      i_capacity: "",
      i_manUsername: null
    }
    this.createTheater = this.createTheater.bind(this)
    this.validateState = this.validateState.bind(this)
  }

  createTheater() {
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var requestBody = JSON.parse(JSON.stringify(this.state))
      
      var doQuery = this.validateState(requestBody)
      if (doQuery) {
        var apiClient = new APIClient(accessToken)

        requestBody.i_comName = requestBody.i_comName['value']
        requestBody.i_thState = requestBody.i_thState['value']
        requestBody.i_manUsername = requestBody.i_manUsername['value']['username']
        
        
        apiClient.perform("post", "/theater", requestBody)
        .then( resp => {
          window.alert("Created Theater")

        })
        .catch( error => {
          window.alert(`Error talking to server ${error.message}`)
        })

      }
      
    }
  }

  validateState(requestBody) {
    var doQuery = true
      if (requestBody.i_thName === "") {
        window.alert("Please input a theater Name")
        doQuery = false
      } else if (requestBody.i_comName == null) {
        window.alert("Please select a company Name")
        doQuery = false
      } else if (requestBody.i_thStreet === "") {
        window.alert("Please input a Street Address")
        doQuery = false
      } else if (requestBody.i_thCity === "") {
        window.alert("Please input a City for address")
        doQuery = false
      } else if (requestBody.i_thState == null) {
        window.alert("Please select a State for address")
        doQuery = false
      } else if (requestBody.i_thZipcode === "") {
        window.alert("Please input a Zipcode for address")
        doQuery = false
      } else if (requestBody.i_capacity === "") {
        window.alert("Please input a valid capacity")
        doQuery = false
      } else if (requestBody.i_manUsername == null) {
        window.alert("Please select a valid Manager Name")
        doQuery = false
      } else if(requestBody.i_thStreet.length > 128) {
        window.alert("Address is too long");
        doQuery = false;
      } else if(requestBody.i_thZipcode.length !== 5) {
        window.alert("Zipcode must be 5 characters long");
        doQuery = false;
      } else if(requestBody.i_thZipcode.match(/^[0-9]+$/) == null) {
        window.alert("Zipcode must be only numbers");
        doQuery = false;
      } else if(requestBody.i_capacity.match(/^[0-9]+$/) == null || requestBody.i_capacity <= 0) {
        window.alert("Please input a valid capacity");
        doQuery = false;
      } else if (requestBody.i_thState['value'] == "ALL") {
        window.alert("State cannot be ALL");
        doQuery = false;
      } else if (requestBody.i_manUsername['value'] == "ALL") {
        window.alert("Manager cannot be ALL");
        doQuery = false;
      } else if (requestBody.i_comName['value'] == "ALL") {
        window.alert("Company cannot be ALL")
        doQuery = false;
      }
      return doQuery;
  }


  render () {
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Create Theater</h2>
          </div>
          <div className="card-body">
            <div className="row">
              <div className="form-inline functionalities-form-row">
                <label>Name</label>
                <input className="form-control"
                  value={this.state.i_thName}
                  onChange={(event) => this.setState({i_thName: event.target.value})}
                />
                <div className="col"></div>
                <label>Company</label>
                <Select className="functionalities-select"
                  value={this.state.i_comName}
                  options={getCompanies()}
                  onChange={com => this.setState({i_comName: com})}
                />
              </div>
              
            </div>
            <div className="row functionalities-form-row form-inline">
              <label>Street Address</label>
              <input className="form-control col-9"
                value={this.state.i_thStreet}
                onChange={(event) => this.setState({i_thStreet: event.target.value})}
              />
            </div>
            <div className="row functionalities-form-row form-inline">
              <label className="col-1">City</label>
              <input className="form-control"
                value={this.state.i_thCity}
                onChange={(event) => this.setState({i_thCity: event.target.value})}
              />
              <label className="col-1">State</label>
              <Select className="col-2"
                value={this.state.i_thState}
                options={stateOptions()}
                onChange={state => this.setState({i_thState: state})}
              />
              <label className="col-1">Zipcode</label>
              <input className="form-control col-2"
                value={this.state.i_thZipcode}
                onChange={(event) => this.setState({i_thZipcode: event.target.value})}
              />
            </div>
            <div className="row functionalities-form-row form-inline">
              <label>Capacity</label>
              <input className="form-control"
                value={this.state.i_capacity}
                onChange={(event) => this.setState({i_capacity: event.target.value})}
              />
              <label>Manager</label>
              <Select className="functionalities-select"
                value={this.state.i_manUsername}
                options={managers()}
                onChange={man => this.setState({i_manUsername: man})}
              />
            </div>
          </div>
          
          <div className="row">
            <a className="btn btn-primary" href="/auth/Manage-Company">Back</a>
            <button className="btn btn-primary" onClick={this.createTheater}>Create</button>
          </div>
        </div>
      </div>
    )
  }
}