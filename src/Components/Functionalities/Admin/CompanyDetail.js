import React, { Component } from 'react'
import APIClient from "../../../apiClient"

import "../Functionality.css"

export default class CompanyDetail extends Component {
  constructor(props) {
    super(props)
    var comName = this.props.match.params["name"]
    this.state = {
      emplList: ["Cole h", "rebecka", "jjj"],
      rowData: [[],[],[],[],[],[]],
      comName: comName
    }
    console.log(props)
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      console.log(apiClient)

    }
  }


  render () {
    return (
      <div className="main">
        <div className="card">
          <div className="card-header">
            <h2>Company Detail</h2>
          </div>
          <div className="card-body">
            <div className="row">
              <h4 className="col-3">Name: </h4>
              <div className="col text-left">{this.state.comName}</div>
            </div>
          
            <div className="row">
              <h4 className="col-3">Employees: </h4>
              <div className="col text-left">
                {this.state.emplList.map( empl => {
                  var keyV = this.state.emplList.indexOf(empl)
                  var element = <span key={keyV}>{empl}, </span>
                  if (keyV >= this.state.emplList.length - 1) {
                    element = <span key={keyV}>{empl}</span>
                  }
                  return (
                    element
                  );
                })}
              </div>
            </div>

            <div className="row">
              <h3 className="col">Theaters</h3>
            </div>


          <div className="functionalities-table">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Manager</th>
                <th scope="col">City</th>
                <th scope="col">State</th>
                <th scope="col">Capacity</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
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