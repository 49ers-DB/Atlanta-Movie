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
    this.setMovieName = this.setMovieName.bind(this)
    this.setMovieDur1 = this.setMovieDur1.bind(this)
    this.setMovieDur2 = this.setMovieDur2.bind(this)
    this.setMovRelDate1 = this.setMovRelDate1.bind(this)
    this.setMovRelDate2 = this.setMovRelDate2.bind(this)
    this.setMovPlayDate1 = this.setMovPlayDate1.bind(this)
    this.setMovPlayDate2 = this.setMovPlayDate2.bind(this)
    this.setInclude = this.setInclude.bind(this)
    this.handleFilter = this.handleFilter.bind(this)
    
    this.handleFilter(new Event(""))
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)

    }
  }

  setMovieName(event) {
    this.setState({movieName: event.target.value})
  }

  setMovieDur1(event) {
    this.setState({movieDuration1: event.target.value})
  }

  setMovieDur2(event) {
    this.setState({movieDuration2: event.target.value})
  }

  setMovRelDate1(movieReleaseDate1) {
    this.setState({movieReleaseDate1})
  }

  setMovRelDate2(movieReleaseDate2) {
    this.setState({movieReleaseDate2})
  }

  setMovPlayDate1(moviePlayDate1) {
    this.setState({moviePlayDate1})
  }

  setMovPlayDate2(moviePlayDate2) {
    this.setState({moviePlayDate2})
  }

  setInclude(event) {
    this.setState({includeNotPlayed: event.target.value})
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
                <input className="form-control" onChange={this.setMovieName} value={this.state.movieName}></input>
                <label>Movie Duration</label>
                <input className="form-control col-1" onChange={this.setMovieDur1} value={this.state.movieDuration1}></input>
                <div>--</div>
                <input className="form-control col-1" onChange={this.setMovieDur2} value={this.state.movieDuration2}></input>
              </div>
            </div>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col-9">
                <label>Movie Release Date</label>
                <DatePicker className="form-control"
                value={this.state.movieReleaseDate1}
                selected={this.state.movieReleaseDate1}
                onChange={this.setMovRelDate1}
                />
                <div className="col-1">--</div>
                <DatePicker className="form-control"
                value={this.state.movieReleaseDate2}
                selected={this.state.movieReleaseDate2}
                onChange={this.setMovRelDate2}
                />
              </div>
              <div className="form-group form-inline functionalities-form-row col-9">
                <label>Movie Play Date</label>
                <DatePicker className="form-control"
                value={this.state.moviePlayDate1}
                selected={this.state.moviePlayDate1}
                onChange={this.setMovPlayDate1}
                />
                <div className="col-1">--</div>
                <DatePicker className="form-control"
                value={this.state.moviePlayDate2}
                selected={this.state.moviePlayDate2}
                onChange={this.setMovPlayDate2}
                />
              </div>
            </div>
            <div>
              
              <input type="checkbox" onChange={this.setInclude} value={this.state.includeNotPlayed}></input>
              <label> Only include not played movies</label>
  
            </div>
            <div className="row">
              <button className="btn btn-primary" onClick={this.handleFilter}>
                Filter
              </button>
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