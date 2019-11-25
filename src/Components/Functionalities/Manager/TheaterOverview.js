import React, { Component } from 'react'
import DatePicker from 'react-datepicker'
import APIClient from "../../../apiClient"

import "../Functionality.css"

export default class TheaterOverview extends Component {
  constructor(props) {
    super(props)
    this.state = {
      rowData: [[],[],[],[],[],[]],
      movieName: "",
      movieDuration1: "",
      movieDuration2: "",
      movieReleaseDate1: null,
      movieReleaseDate2: null,
      moviePlayDate1: null,
      moviePlayDate2: null,
      includeNotPlayed: false
    }
    
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
            <h2>Theater Overview</h2>
          </div>
          <div className="card">
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col">
                <label>Movie Name</label>
                <input className="form-control"></input>
                <label>Morning Duration</label>
                <input className="form-control col-1"></input>
                <div>--</div>
                <input className="form-control col-1"></input>
              </div>
            </div>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col-9">
                <label>Movie Release Date</label>
                <DatePicker className="form-control"/>
                <div className="col-1">--</div>
                <DatePicker className="form-control"/>
              </div>
              <div className="form-group form-inline functionalities-form-row col-9">
                <label>Movie Play Date</label>
                <DatePicker className="form-control"/>
                <div className="col-1">--</div>
                <DatePicker className="form-control"/>
              </div>
            </div>
            <div>
              <div>
                
                <input type="checkbox"></input>
                <label> Only include not played movies</label>
              </div>
            </div>
            
            <div className="functionalities-table">
            <table className="table">
              <thead>
                <tr>
                  <th scope="col">Movie Name</th>
                  <th scope="col">Duration</th>
                  <th scope="col">Release Date</th>
                  <th scope="col">Play Date</th>
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