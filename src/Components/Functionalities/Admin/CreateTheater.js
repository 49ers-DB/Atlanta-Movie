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
    
   
  }

  createTheater() {
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      
    }
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
                value={this.state.i_thState}
                onChange={(event) => this.setState({i_thState: event.target.value})}
              />
              <label className="col-1">State</label>
              <Select className="col-2"
                value={this.state.i_thState}
                options={stateOptions()}
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