import React, { Component } from 'react'
import APIClient from "../../../apiClient"
import Select from 'react-select'

import "../Functionality.css"

export default class ManageCompany extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [[],[]],
      selectedComName: null,
      numCitiesCov1: "",
      numCitiesCov2: "",
      numTheaters1: "",
      numTheaters2: "",
      numEmployees1: "",
      numEmployees2: "",
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
        <div className="card">
          <div className="card-header">
            <h2>Manage Company</h2>
          </div>
          <div className="card-body">
            <div className="row">
              <div className="form-group form-inline functionalities-form-row">
                <label>Name</label>
                <Select className="functionalities-select"
                />
                <label>Num. Cities Covered</label>
                <input className="form-control col-1"/>
                <div>--</div>
                <input className="form-control col-1"/>
              </div>

            </div>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row">
                <label>Num. Theaters</label>
                <input className="form-control col-1"/>
                <div>--</div>
                <input className="form-control col-1"/>
                <label>Num. Employees</label>
                <input className="form-control col-1"/>
                <div>--</div>
                <input className="form-control col-1"/>
              </div>
            </div>
            <div className="row">
              <button className="btn btn-primary col-3">Filter</button>
              <div className="col-3"></div>
              <a className="btn btn-primary col-2" href="/">Create Theater</a>
              <button className="btn btn-primary col-2" href="/">Detail</button>
            </div>
            
            <div className="functionalities-table visitHistoryTableCard">
            <table className="table">
              <thead>
                <tr>
                  <th scope="col">Selected</th>
                  <th scope="col">Name</th>
                  <th scope="col">Num. Cities Covered</th>
                  <th scope="col">Num. Theaters</th>
                  <th scope="col">Num. Employees</th>
                </tr>
              </thead>
              <tbody>
                
                  {this.state.rowData.map( (row) => {
                    var index= this.state.rowData.indexOf(row)
                    return (
                      <tr key={this.state.rowData.indexOf(row)}>
                        <td><input type="radio" id={index}/></td>
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