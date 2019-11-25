import React, { Component } from 'react'
import APIClient from "../../../apiClient"
import Select from 'react-select'

import "../Functionality.css"

export default class CreateTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [[],[],[],[],[],[]],
    }
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      this.state.apiClient = apiClient
      console.log(apiClient)


      

    //   apiClient.perform('post', '/visitHistory', this.state).then(resp => {
    //     var rowData = resp
    //     this.state.rowData = rowData
    //   });
      
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
                />
                <div className="col"></div>
                <label>Company</label>
                <Select className="functionalities-select"
                />
              </div>
              
            </div>
            <div className="row functionalities-form-row form-inline">
              <label>Street Address</label>
              <input className="form-control col-9"/>
            </div>
            <div className="row functionalities-form-row form-inline">
              <label className="col-1">City</label>
              <input className="form-control"></input>
              <label className="col-1">State</label>
              <Select className="col-2"
              />
              <label className="col-1">Zipcode</label>
              <input className="form-control col-2"/>
            </div>
            <div className="row functionalities-form-row form-inline">
              <label>Capacity</label>
              <input className="form-control"/>
              <label>Manager</label>
              <Select className="functionalities-select"
              />
            </div>

          </div>
          
          <div className="row">
            <a className="btn btn-primary" href="/auth/Manage-Company">Back</a>
            <button className="btn btn-primary">Create</button>
          </div>
          

        </div>
          
      </div>
    )
  }
}