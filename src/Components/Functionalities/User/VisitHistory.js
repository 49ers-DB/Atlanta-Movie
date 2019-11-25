import React, { Component } from 'react'
import DatePicker from "react-datepicker";
import Select from "react-select";
import APIClient from "../../../apiClient"
import toDateString from '../../../actions/date'

import "../Functionality.css"

import "react-datepicker/dist/react-datepicker.css";


export default class VisitHistory extends Component {
  constructor(props) {
    super(props)
    this.state = {
      apiClient: null,
      rowData: [],
      companies: [],
      selectedCompany: null,
      visitDate1: null,
      visitDate2: null,
    }
    
    this.handleFilter = this.handleFilter.bind(this)
    this.handleChange1 = this.handleChange1.bind(this)
    this.handleChange2 = this.handleChange2.bind(this)
    this.setSelectedCompany = this.setSelectedCompany.bind(this)

    this.handleFilter(new Event(""))
  }


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

      var requestBody = JSON.parse(JSON.stringify(this.state))
      if (requestBody.visitDate1) {
        requestBody.visitDate1 = toDateString(this.state.visitDate1.toDateString())
      }
      
      if (requestBody.visitDate2) {
        requestBody.visitDate2 = toDateString(this.state.visitDate2.toDateString())
      }

      apiClient.perform('post', '/GetVisitHistory', requestBody ).then( resp => {
        this.setState({rowData: resp['data']},
        console.log(resp))
      });
      
    }

      
    
  }


//   handleChange = event => {
//     this.setState({[event.target.name]: event.target.value});
//   }

  handleChange1(date) {
    this.setState({visitDate1: date})
  }
  handleChange2(date) {
    this.setState({visitDate2: date})
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
                            onChange={this.handleChange1}
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
                            onChange={this.handleChange2}
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
              
                {
                  
                this.state.rowData.map( (row) => {
                  if(this.state.rowData.length > 0) {
                    var date = toDateString(row['visitDate'])
                  var address = row['thStreet']  + ', ' + row['thCity'] + ', ' + row['thState'] + ' ' + row['thZipcode']
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
                      <td>{row['thName']}</td>
                      <td>{address}</td>
                      <td>{row['comName']}</td>
                      <td>{date}</td>
                    </tr>
                  );
                  }
                  
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
