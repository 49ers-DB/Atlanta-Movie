import React, { Component } from 'react'
import DatePicker from "react-datepicker";
import Select from "react-select";
import AsyncSelect from 'react-select/async';
import APIClient from "../../../apiClient"

import "../Functionality.css"

import "react-datepicker/dist/react-datepicker.css";

const stateOptions = [
  {value: "AL", label: "AL"},
  {value: "AK", label: "AK"},
  {value: "AZ", label: "AZ"},
  {value: "AR", label: "AR"},
  {value: "CA", label: "CA"},
  {value: "CO", label: "CO"},
  {value: "CT", label: "CT"},
  {value: "DE", label: "DE"},
  {value: "FL", label: "FL"},
  {value: "GA", label: "GA"},
  {value: "HI", label: "HI"},
  {value: "ID", label: "ID"},
  {value: "IL", label: "IL"},
  {value: "IN", label: "IN"},
  {value: "IA", label: "IA"},
  {value: "KS", label: "KS"},
  {value: "KY", label: "KY"},
  {value: "LA", label: "LA"},
  {value: "ME", label: "ME"},
  {value: "MD", label: "MD"},
  {value: "MA", label: "MA"},
  {value: "MI", label: "MI"},
  {value: "MN", label: "MN"},
  {value: "MS", label: "MS"},
  {value: "MO", label: "MO"},
  {value: "MT", label: "MT"},
  {value: "NE", label: "NE"},
  {value: "NV", label: "NV"},
  {value: "NH", label: "NH"},
  {value: "NJ", label: "NJ"},
  {value: "NM", label: "NM"},
  {value: "NY", label: "NY"},
  {value: "NC", label: "NC"},
  {value: "ND", label: "ND"},
  {value: "OH", label: "OH"},
  {value: "OK", label: "OK"},
  {value: "OR", label: "OR"},
  {value: "PA", label: "PA"},
  {value: "RI", label: "RI"},
  {value: "SC", label: "SC"},
  {value: "SD", label: "SD"},
  {value: "TN", label: "TN"},
  {value: "TX", label: "TX"},
  {value: "UT", label: "UT"},
  {value: "VT", label: "VT"},
  {value: "VA", label: "VA"},
  {value: "WA", label: "WA"},
  {value: "WV", label: "WV"},
  {value: "WI", label: "WI"},
  {value: "WY", label: "WY"},
]

var theaters = []

export default class ExploreTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [["fj","fjdk","fjd"],[],[],[]],
      theaters: [],
      companies: [],
      city: "",
      selectedTheater: null,
      selectedCompany: null,
      selectedState: null,
      visitDate: new Date()
    }
    
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      this.state.apiClient = apiClient
      console.log(apiClient)

      apiClient.perform('get', '/exploreTheater', this.state).then(resp => {
        var rowData = resp
        this.state.rowData = rowData
      });
      
    }
    this.handleLogVisit = this.handleLogVisit.bind(this)
    this.handleFilter = this.handleFilter.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.setSelectedTheater = this.setSelectedTheater.bind(this)
    this.setSelectedCompany = this.setSelectedCompany.bind(this)
    this.setSelectedState = this.setSelectedState.bind(this)
    this.setCity = this.setCity.bind(this)
    // this.componentDidMount = this.componentDidMount.bind(this)
    this.getTheatersForCompany = this.getTheatersForCompany.bind(this)
  }

  // componentDidMount() {
  //   this.getTheatersForCompany("")
  // }

  getTheatersForCompany(companyName) {
    var accessToken = localStorage.getItem("accessToken")
    theaters = []
    this.setState({selectedTheater: null})
    
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
  

  getCompanies() {
    var companies = []
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      apiClient.getCompanies().then( resp => {
        for(var i = 0; i < resp.length; i++) {
          var companyName = resp[i].comName;
          companies[i] = {value: companyName, label: companyName}
        }
      });
    
    }
    return companies;
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)

      apiClient.perform('get', '/exploreTheater', this.state).then( resp => {

      });
      
    }
  }

  handleLogVisit(event) {
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      this.state.apiClient = apiClient
      console.log(apiClient)

      apiClient.perform('post', '/logVisit', this.state).then( resp => {

      });
      
    }
  }

  handleChange(date) {
    this.setState({visitDate: date})
  }

  setSelectedTheater = (selectedTheater) => {
    this.setState({selectedTheater})
  }

  setSelectedCompany = (selectedCompany) =>  {
    this.setState({selectedCompany})
    var company = selectedCompany['value']
    this.getTheatersForCompany(company)
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
        <div className="card registrationCard">
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
                  options={this.getCompanies()}
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
                  options={stateOptions}
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
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
                      <td>
                        <input type="checkbox" className="form-check-input" id=""/>
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
