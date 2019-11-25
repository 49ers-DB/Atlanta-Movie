import React, { Component } from 'react'
import APIClient from "../../../apiClient"
import Select from 'react-select'
import DatePicker from 'react-datepicker'
import stateOptions from "../../../actions/stateOptions"
import getCompanies from "../../../actions/companies"
import movies from "../../../actions/movies"

import "../Functionality.css"
import { isThisISOWeek } from 'date-fns'




function formatRows(data) {
  console.log(data)
  var formatted = []

  data.map( row => {
    var addressStr = `${row['thStreet']}, ${row['thCity']}, ${row['thState']}, ${row['thZipcode']}`
    var date = new Date(row['movPlayDate'])
    console.log(date)
    date = date.toDateString()
    formatted.push([row['movName'], row['thName'], addressStr, row['comName'], date])
  });
  return formatted
}

export default class ExploreMovie extends Component {
  constructor(props) {
    super(props)
    this.state = {
      rowData: [],
      selectedMovie: null,
      selectedCompany: null,
      city: "",
      selectedState: "",
      playDate1: null,
      playDate2: null,
      moviePlayIndex: null,
      selectedCreditCard: null
    }
    this.setSelectedMovie = this.setSelectedMovie.bind(this)
    this.setSelectedCompany = this.setSelectedCompany.bind(this)
    this.setSelectedState = this.setSelectedState.bind(this)
    this.setCity = this.setCity.bind(this)
    this.setPlayDate1 = this.setPlayDate1.bind(this)
    this.setPlayDate2 = this.setPlayDate2.bind(this)
    this.setCreditCard = this.setCreditCard.bind(this)
    this.handleFilter = this.handleFilter.bind(this)
    this.handleView = this.handleView.bind(this)
    
    this.handleFilter(new Event(""))
    
  }

  setSelectedMovie(event) {
    this.setState({selectedMovie: event})
  }

  setSelectedCompany(selectedCompany) {
    this.setState({selectedCompany})
  }

  setCity(event) {
    this.setState({city: event.target.value})
  }

  setSelectedState(selectedState) {
    this.setState({selectedState})
  }

  setPlayDate1(playDate1) {
    this.setState({playDate1})
  }

  setPlayDate2(playDate2) {
    this.setState({playDate2})
  }

  checkedMoviePlay(moviePlayIndex) {
    this.setState({moviePlayIndex})
  }

  getCreditCards() {
    var accessToken = localStorage.getItem("accessToken")
    
    var creditcards = []
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      apiClient.perform("get", "/creditcard").then( resp => {

        resp.map( creditCard => {
          var num = creditCard['creditCardNum']
          creditcards.push({value: num, label: num})
        })
        
      });
    }
    return creditcards
  }

  setCreditCard(selectedCreditCard) {
    this.setState(selectedCreditCard)
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      var com = this.state.selectedCompany
      if (com) {com = com['value']}
      var mov = this.state.selectedMovie
      if (mov) {mov = mov['value']}
      var stateName = this.state.selectedState
      if (stateName) {stateName = stateName['value']}


      var requestBody = {
        i_movName: mov,
        i_comName: com,
        i_city: this.state.city,
        i_state: stateName,
        i_minMovPlayDate: this.state.playDate1,
        i_maxMovPlayDate: this.state.playDate2
      }
      console.log(requestBody)
      apiClient.perform("post", "/exploreMovie", requestBody).then( resp => {
        this.setState({rowData: formatRows(resp['moviePlays'])})
      })
    }
  }

  handleView(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken && this.state.moviePlayIndex) {
      var apiClient = new APIClient(accessToken)
      var requestBody = {
        i_movName: this.state.rowData[this.state.moviePlayIndex][0],
        i_thName: this.state.rowData[this.state.moviePlayIndex][1],
        i_comName: this.state.rowData[this.state.moviePlayIndex][3],
        i_movPlayDate: this.state.rowData[this.state.moviePlayIndex][4],
        i_creditCardNum: this.state.selectedCreditCard['value']
      }
      apiClient.perform("post", "/viewMovie", requestBody)
    }
  }

  render () {
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Explore Movie</h2>
          </div>

          <form>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">Movie Name</label>
                <Select className="functionalities-select"
                  value={this.state.selectedMovie}
                  onChange={this.setSelectedMovie}
                  options={movies()}
                />
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="comName">Company Name</label>
                <Select className="functionalities-select"
                  value={this.state.selectedCompany}
                  onChange={this.setSelectedCompany}
                  options={getCompanies()}
                  cacheOptions 
                />
              </div>  
            </div>
            <div className="row">
            <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">City</label>
                <input className="form-control functionalities" value={this.state.city} onChange={this.setCity}/>
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="comName">State</label>
                <Select className="functionalities-select"
                  value={this.state.selectedState}
                  onChange={this.setSelectedState}
                  options={stateOptions()}
                />
              </div>  
            </div>
            <div className="row form-inline functionalities-form-row">
                <div className="col-6">
                    <div className="row">
                        <div className="col-4">
                            <label>Movie Play Date</label>
                        </div>
                        <div className="col-8">
                            <DatePicker className="form-control"
                            value={this.state.playDate1}
                            selected={this.state.playDate1}
                            onChange={this.setPlayDate1}
                            />
                        </div>
                    </div>
                </div>
                <div className="col-6">
                    <div className="row">
                        <div className="col-2">
                            <label>--</label>
                        </div>
                        <div className="col-8">
                            <DatePicker className="form-control"
                            value={this.state.playDate2}
                            selected={this.state.playDate2}
                            onChange={this.setPlayDate2}
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
              <button className="btn btn-primary" onClick={this.handleFilter}>Filter</button>
            </div>
          </form>
          <div className="functionalities-table">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Selected</th>
                <th scope="col">Movie</th>
                <th scope="col">Theater</th>
                <th scope="col">Address</th>
                <th scope="col">Company</th>
                <th scope="col">Play Date</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  var index = this.state.rowData.indexOf(row)
                  return (
                    <tr key={index}>
                      <td>
                        <input type="radio" name="optradio" id={index} onClick={ () => this.checkedMoviePlay(index) }/>
                      </td>
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
          <div className="row">
            <div className="col-3">
              <a className="btn btn-primary" href="/menu">Back</a>
            </div>
            <div className="col form-inline functionalities-form-row">
                <label>Credit Card</label>
                <Select className="functionalities-select"
                  selected={this.state.selectedCreditCard}
                  onChange={this.setCreditCard}
                  options={this.getCreditCards()}
                />
            </div>
            <div className="col-3">
              <button className="btn btn-primary" onClick={this.handleView}>View</button>
            </div>
              
              
            
          </div>
          

        </div>
          
      </div>
    )
  }
}