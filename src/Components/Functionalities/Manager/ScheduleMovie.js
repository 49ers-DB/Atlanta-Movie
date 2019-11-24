import React, { Component } from 'react'
import APIClient from "../../../apiClient"
import movies from "../../../actions/movies"
import Select from 'react-select'
import  DatePicker from 'react-datepicker'

import "../Functionality.css"


export default class ScheduleMovie extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [[],[],[],[],[],[]],
      selectedMovie: null,
      releaseDate: null,
      playDate: null
    }
    this.setSelectedMovie = this.setSelectedMovie.bind(this)
    this.handleReleaseDateChange = this.handleReleaseDateChange.bind(this)
    this.handlePlayDateChange = this.handlePlayDateChange.bind(this)
    this.handleAdd = this.handleAdd.bind(this)
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      console.log(apiClient)
      
    }
  }

  setSelectedMovie(event) {
    this.setState({selectedMovie: event.target.value})
  }

  handleReleaseDateChange(releaseDate) {
    this.setState(releaseDate)
  }

  handlePlayDateChange(playDate) {
    this.setState(playDate)
  }

  handleAdd(event) {
    event.preventDefault()
    //TODO ApIcall
  }

  render () {
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Schedule Movie</h2>
          </div>
          <div className="card-body">
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col">
                  <label htmlFor="theaterName">Movie Name</label>
                  <Select className="functionalities-select"
                    value={this.state.selectedMovie}
                    onChange={this.setSelectedMovie}
                    options={null}
                    placeholder="Select"
                  />
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                  <label htmlFor="theaterName">Release Date</label>
                  <DatePicker className="form-control"
                    selected={this.state.releaseDate}
                    onChange={this.handleReleaseDateChange}
                  />
              </div>
            </div>
            <div className="row">
              <div className=" functionalities-form-row col">
                <label htmlFor="theaterName">Play Date</label>
                <DatePicker className="form-control"
                  selected={this.state.playDate}
                  onChange={this.handlePlayDateChange}
                />
              </div>
            </div>
          </div>
          
          <div className="row">
            <div className="col-3">
              <a className="btn btn-primary" href="/menu">Back</a>
            </div>
            <div className="col-6"></div>
            <div className="col-3">
              <button className="btn btn-primary" onClick={this.handleAdd}>Add</button>
            </div>
          </div>
          

        </div>
          
      </div>
    )
  }
}