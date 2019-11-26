import React, { Component } from 'react'
import APIClient from "../../../apiClient"
import DatePicker from "react-datepicker";


import "../Functionality.css"

export default class CreateMovie extends Component {
  constructor(props) {
    super(props)
    this.state = {
      movieName: null,
      duration: null,
      releaseDate: new Date(),
    }
    
    this.handleDateChange = this.handleDateChange.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange = event => {
    this.setState({[event.target.name]: event.target.value});
  }
  handleDateChange(date) {
    this.setState({releaseDate: date})
  }

  createMovie() {
    if(this.state.movieName === null) {
      window.alert("Movie Name must be filled")
    } else if (this.state.releaseDate === null) {
      window.alert("Release Date must be filled")
    } else if(this.state.duration === null) {
      window.alert("Duration must be filled")
    } else if(this.state.duration.match(/^[0-9]+$/) == null) {
      window.alert("You may only enter numbers in Duration")
    } else if(this.state.duration <= 0) {
      window.alert("Duration has to be longer than 0 minutes")
    } else {
      var accessToken = localStorage.getItem("accessToken")
    
      if (accessToken) {
        var apiClient = new APIClient(accessToken)
        this.state.apiClient = apiClient
        apiClient.perform('post', '/createMovie', this.state).then(resp => {
          window.alert(resp['data'])
        });
        
      }

    }
  }
//idiot


  render () {
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Create Movie</h2>          
          </div>
          <div className="movieRegister row">
            <div className="col-6">
              <div className="row">
                <div className="col-4">
                  <label>Movie Name</label>
                </div>
                <div className="col-8">
                  <input type="text" name="movieName" onChange={this.handleChange} className="form-control" id="movieName"/>
                </div>
              </div>
            </div>
            <div className="col-6">
              <div className="row">
                <div className="col-2">
                  <label>Duration</label>
                </div>
                <div className="col-8">
                  <input type="text" name="duration" onChange={this.handleChange} className="form-control" id="duration"/>
                </div>
              </div>
            </div>
          </div>
          <div className="movieRegister row">
            <div className="col-4">
              <label>Release Date</label>
            </div>
            <div className="col-4">
              <DatePicker className="form-control"
              value={this.state.releaseDate}
              selected={this.state.releaseDate}
              onChange={this.handleDateChange}
              />
            </div>
          </div>
          <div className="row">
            <div className="col-6">
              <a className="btn btn-primary" href="/menu">Back</a>
            </div>
            <div className="col-6">
              <div className="btn btn-primary" onClick={() => this.createMovie()}>Create</div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}