import React, { Component } from 'react'
import Select from 'react-select'
import APIClient from "../../../apiClient"

import "../Functionality.css"

const statuses = [
  {value:"All", label:"All"},
  {value:"Approved", label:"Approved"},
  {value:"Pending", label:"Pending"},
  {value:"Declined", label:"Declined"}
]

export default class ManageUser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      username: "",
      rowData: [[],[],[],[],[],[]],
      selectedStatus: null,

    }
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      this.state.apiClient = apiClient
      console.log(apiClient)

    }
  }




  render () {
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Manage User</h2>
          </div>
          <div className="card-body">
            <div className="row form-group">
              <div className="form-inline col">
                <label className="col">Username</label>
                <input className="form-control col-4"
                 value={this.state.username}
                 onChange={(event) => this.setState({username: event.target.value})}/>
                <label className="col">Status</label>
                <Select className="functionalities-select col-4"
                  value={this.state.selectedStatus}
                  options={statuses}
                  onChange={(status) => this.setState({selectedStatus: status})}
                />
              </div>
            </div>
            <div className="row">
                <button className="btn btn-primary col-2">Filter</button>
                <div className="col-3"></div>
                <button className="btn btn-primary col-2">Approve</button>
                <button className="btn btn-primary col-2">Decline</button>
            </div>
          <div className="functionalities-table">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Selected</th>
                <th scope="col">Username</th>
                <th scope="col">Credit Card Count</th>
                <th scope="col">User Type</th>
                <th scope="col">Status</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
                      <td><input type="radio" name="radioclass"/></td>
                      <td>{row[0]}</td>
                      <td>{row[1]}</td>
                      <td>{row[2]}</td>
                      <td>{row[3]}</td>
                      <td>{row[4]}</td>
                    </tr>
                  );
                })}
    
            </tbody>
          </table>
          </div>

          </div>
          
          <div className="row">
            <div className="col-12">
              <a className="btn btn-primary" href="/menu">Back</a>
            </div>
          </div>
          

        </div>
          
      </div>
    )
  }
}