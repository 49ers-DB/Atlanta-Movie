import React, { Component } from 'react'
import APIClient from "../../../apiClient"

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
            <h2>Create Movie</h2>
          </div>
          <div className="card visitHistoryTableCard">
          <div className="functionalities-table">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Movie</th>
                <th scope="col">Theater</th>
                <th scope="col">Company</th>
                <th scope="col">Card#</th>
                <th scope="col">View Date</th>
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