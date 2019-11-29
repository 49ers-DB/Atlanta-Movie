import React, { Component } from 'react'
import DatePicker from "react-datepicker";
import Select from "react-select";
import APIClient from "../../../apiClient"
import stateOptions from "../../../actions/stateOptions"
import getCompanies from "../../../actions/companies"

import "../Functionality.css"

import "react-datepicker/dist/react-datepicker.css";
import { isThisISOWeek } from 'date-fns';


var theaters = []


function formatTheaters(theaters) {
  var formatted = []
  if (theaters) {
    theaters.map( theater => {
      var addressStr = `${theater['thStreet']}, ${theater['thCity']}, ${theater['thState']}, ${theater['thZipcode']}`
      formatted.push([theater['thName'], addressStr, theater['comName']])
    });
  }
  return formatted;
}

export default class ExploreTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [[],[],[],[]],
      theaters: [],
      companies: [],
      city: "",
      selectedTheater: null,
      selectedCompany: null,
      selectedState: null,
      visitDate: new Date(),
      theaterIndex: null,
    }
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      this.state.apiClient = apiClient
      
      apiClient.exploreTheater(this.state).then(resp => {
        this.setState({rowData: formatTheaters(resp['theaters'])})
        console.log(resp['theaters'])
      });
    }
    this.handleLogVisit = this.handleLogVisit.bind(this)
    this.handleFilter = this.handleFilter.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.setSelectedTheater = this.setSelectedTheater.bind(this)
    this.setSelectedCompany = this.setSelectedCompany.bind(this)
    this.setSelectedState = this.setSelectedState.bind(this)
    this.setCity = this.setCity.bind(this)
    this.checkedTheater = this.checkedTheater.bind(this);
    this.getTheatersForCompany = this.getTheatersForCompany.bind(this)
    this.getTheatersForCompany("hello")
  }


  getTheatersForCompany(companyName) {
    var accessToken = localStorage.getItem("accessToken")
    theaters = [{value: "ALL", label: "ALL"}]
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      apiClient.getTheaters(companyName).then( resp => {
        
        var someTheats = resp['theaters']
        someTheats.map( theater => {
          theaters.push({
            value: theater['thName'],
            label: theater['thName']});
        });
      });
    }
  }
  

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)

      var state = this.state.selectedState
      if (state) {state = state['value']}
      var company = this.state.selectedCompany
      if (company) {company = company['value']}
      var theater = this.state.selectedTheater
      if (theater) {theater = theater['value']}


      var requestBody = {
        city: this.state.city,
        selectedState: state,
        selectedCompany: company,
        selectedTheater: theater
      }

      apiClient.perform('post', '/exploreTheater', requestBody).then( resp => {
        this.setState({rowData: formatTheaters(resp['theaters'])})
      });
      
    }
  }

  handleLogVisit(event) {
    if(this.state.theaterIndex === null) {
      window.alert("Please choose a theater")
      return;
    }
    var theater = this.state.rowData[this.state.theaterIndex];
    var data = {i_thname: theater[0],
            i_coname: theater[2],
            i_visitdate: this.state.visitDate}
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      this.state.apiClient = apiClient
      console.log(apiClient)

      apiClient.perform('post', '/logVisit', data).then( resp => {
        window.alert("User Visit Logged")
      })
      .catch( error => {
         window.alert("Error Logging Visit")
      })
      
    }
  }

  checkedTheater(index) {
    this.setState({theaterIndex: index})
  }

  handleChange(date) {
    this.setState({visitDate: date})
  }

  setSelectedTheater = (selectedTheater) => {
    this.setState({selectedTheater})
  }

  setSelectedCompany = (selectedCompany) =>  {
    this.setState({selectedCompany})
  }

  setSelectedState = (selectedState) => {
    this.setState({selectedState})
  }

  setCity = (event) => {
    this.setState({city: event.target.value})
  }

  render () {
    return (
      <div className="main">
        <div className="card exploreTheaterCard">
          <div className="card-header">
            <h2>Explore Theater</h2>
          </div>

          <form>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">Theater Name</label>
                <Select className="functionalities-select"
                  value={this.state.selectedTheater}
                  onChange={this.setSelectedTheater}
                  options={theaters}
                  placeholder="Select"
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
                  placeholder="Select"
                />
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
                <th scope="col">Theater</th>
                <th scope="col">Address</th>
                <th scope="col">Company</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  var index = this.state.rowData.indexOf(row)
                  return (
                    <tr key={index}>
                      <td>
                        <input type="radio" name="optradio" id={index} onClick={ () => this.checkedTheater(index) }/>
                      </td>
                      <td>{row[0]}</td>
                      <td>{row[1]}</td>
                      <td>{row[2]}</td>
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
            <div className="col functionalities-form-row">
                <label>Visit Date</label>
                <DatePicker className="form-control"
                  selected={this.state.visitDate}
                  onChange={this.handleChange}
                />
            </div>
            <div className="col-3">
              <button className="btn btn-primary" onClick={this.handleLogVisit}>Log Visit</button>
            </div>
              
              
            
          </div>
          

        </div>
          
      </div>
    )
  }
}
