import React, { Component } from 'react'
import DatePicker from "react-datepicker";
import Select from "react-select";
import APIClient from "../../../apiClient"

import "../Functionality.css"

import "react-datepicker/dist/react-datepicker.css";


export default class ExploreTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [[],[],[],[],[]],
      companies: [],
      selectedCompany: null,
      visitDate1: null,
      visitDate2: null,
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
    this.handleFilter = this.handleFilter.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.setSelectedCompany = this.setSelectedCompany.bind(this)
  }


  promiseTheaterOptions = inputValue =>
  new Promise();


  getCompanies() {
    var companies = []
    var apiClient = new APIClient("")
        apiClient.getCompanies().then( resp => {
            for(var i = 0; i < resp.length; i++) {
                var companyName = resp[i].comName;
                companies[i] = {value: companyName, label: companyName}
            }
        });
    return companies;
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)

    //   apiClient.perform('post', '/visitHistory', this.state ).then( resp => {

    //   });
      
    }
  }


  handleChange = event => {
    this.setState({[event.target.name]: event.target.value});
  }



  setSelectedCompany = (selectedCompany) =>  {
    this.setState({selectedCompany})
  }


  render () {
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Visit History</h2>
          </div>

          <form>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col-12">
                <div className="col-4">
                    <label htmlFor="comName">Company Name</label>
                </div>
                <div className="col-6">
                    <Select
                    value={this.state.selectedCompany}
                    onChange={this.setSelectedCompany}
                    options={this.getCompanies()}
                    placeholder="None"
                    />
                </div>
              </div>  
            </div>
            <div className="row form-inline functionalities-form-row">
                <div className="col-6">
                    <div className="row">
                        <div className="col-4">
                            <label>Visit Date</label>
                        </div>
                        <div className="col-8">
                            <DatePicker className="form-control"
                            value={this.state.visitDate1}
                            selected={this.state.visitDate1}
                            onChange={this.handleChange}
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
                            value={this.state.visitDate2}
                            selected={this.state.visitDate2}
                            onChange={this.handleChange}
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
              <button className="btn btn-primary" onClick={this.handleFilter}>Filter</button>
            </div>
          </form>
          <div className="card visitHistoryTableCard">
          <div className="functionalities-table">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Theater</th>
                <th scope="col">Address</th>
                <th scope="col">Company</th>
                <th scope="col">Visit Date</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
                      <td>{row[0]}</td>
                      <td>{row[1]}</td>
                      <td>{row[2]}</td>
                      <td>{row[2]}</td>
                    </tr>
                  );
                })}
    
            </tbody>
          </table>
          </div>

          </div>
          
          <div className="row">
            <div className="col-12">
              <a className="btn btn-primary" href="/">Back</a>
            </div>
          </div>
          

        </div>
          
      </div>
    )
  }
}
