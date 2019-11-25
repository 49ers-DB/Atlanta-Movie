import React, { Component } from 'react'
import APIClient from "../../../apiClient"

import "../Functionality.css"

export default class CompanyDetail extends Component {
  constructor(props) {
    super(props)
    var comName = this.props.match.params["name"]
    this.state = {
      emplList: [],
      rowData: [],
      comName: comName
    }
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)

      apiClient.perform("get", "/companyDetail/" + this.state.comName).then( resp => {
        console.log(resp)
        this.setState({
          emplList: resp['employees'],
          rowData: resp['theaters']
        })
        
      }).catch( error => {
        window.alert("Could not find that company")
      })
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
                  var name = empl['firstname'] + " " + empl['lastname']
                  var element = <span key={keyV}>{name}, </span>
                  if (keyV >= this.state.emplList.length - 1) {
                    element = <span key={keyV}>{name}</span>
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
                  var manager = row['firstname'] + " " + row['lastname']
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
                      <td>{row['thName']}</td>
                      <td>{manager}</td>
                      <td>{row["thCity"]}</td>
                      <td>{row['thState']}</td>
                      <td>{row['capacity']}</td>
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