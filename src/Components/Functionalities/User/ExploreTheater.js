import React, { Component } from 'react'
import DatePicker from "react-datepicker";
import Select from "react-select";
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

export default class ExploreTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      rowData: [
        ["","fdasfa",""],
        ["","2",""]
      ],
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
      console.log(apiClient)

      this.props.apiClient.getTheaters().then(resp => {
        var companies = resp.get('')
      });
      this.props.apiClient.getCompanies().then(resp => {

      });
      
    }
  }

  handleFilter(event) {
    event.preventDefault()
  }

  handleLogVisit(event) {
    event.preventDefault()
  }

  handleChange(event) {
    
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
                  options={this.state.theaters}
                  placeholder="Select"
                />
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="comName">Company Name</label>
                <Select className="functionalities-select"
                  value={this.state.selectedCompany}
                  onChange={this.setSelectedCompany}
                  options={this.state.companies}
                  placeholder="Select"
                />
              </div>  
            </div>
            <div className="row">
            <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">City</label>
                <input className="form-control functionalities" id="city"/>
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
                <th scope="col">Theater</th>
                <th scope="col">Address</th>
                <th scope="col">Company</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
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
              <a className="btn btn-primary" href="/">Back</a>
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