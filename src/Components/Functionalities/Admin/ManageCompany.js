import React, { Component } from 'react'
import {Redirect} from 'react-router-dom'
import APIClient from "../../../apiClient"
import Select from 'react-select'


import "../Functionality.css"
import getCompanies from '../../../actions/companies'

export default class ManageCompany extends Component {
  constructor(props) {
    super(props)
    this.state = {
      redirect: false,
      rowData: [['ABC Company']],
      selectedComName: null,
      numCitiesCov1: "",
      numCitiesCov2: "",
      numTheaters1: "",
      numTheaters2: "",
      numEmployees1: "",
      numEmployees2: "",
      companyIndex: null
    }
    this.handleFilter = this.handleFilter.bind(this)
    this.handleCompDetail = this.handleCompDetail.bind(this)
    this.renderRedirect = this.renderRedirect.bind(this)

    this.handleFilter(new Event(""))
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
   
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      var requestBody = {
        i_comName: this.state.selectedComName,
        i_minCity: this.state.numCitiesCov1,
        i_maxCity: this.state.numCitiesCov2,
        i_minTheater: this.state.numTheaters1,
        i_maxTheater: this.state.numTheaters2,
        i_minEmployee: this.state.numEmployees1,
        i_maxEmployee: this.state.numEmployees2
      }
      
      apiClient.perform('post', '/manageCompany', requestBody)
      .then( resp => {
        
      })
      .catch( error => {
        window.alert(`Error talking to server ${error.message}`)
      })
      
    }
  }

  handleCompDetail(event) {
    console.log('redirecting')
    if (this.state.companyIndex || this.state.companyIndex === 0) {
      this.setState({redirect: true})
    } else {
      window.alert("Please Select a Company from the Table")
    }
  }

  renderRedirect = () => {
    if (this.state.redirect) {
      var comName = this.state.rowData[this.state.companyIndex][0]
      return <Redirect to={'/Auth/Company-Detail/' + comName}/>
    }
  }


  render () {
    return (
      <div className="main">
        {this.renderRedirect()}
        <div className="card">
          <div className="card-header">
            <h2>Manage Company</h2>
          </div>
          <div className="card-body">
            <div className="row">
              <div className="form-group form-inline functionalities-form-row">
                <label>Name</label>
                <Select className="functionalities-select"
                value={this.selectedComName}
                onChange={(selected) => this.setState({selectedComName: selected})}
                options={getCompanies()}
                />
                <label>Num. Cities Covered</label>
                <input className="form-control col-1"
                value={this.state.numCitiesCov1}
                onChange={(event) => this.setState({numCitiesCov1: event.target.value})}/>
                <div>--</div>
                <input className="form-control col-1" 
                value={this.state.numCitiesCov2}
                onChange={(event) => this.setState({numCitiesCov2: event.target.value})}
                />
              </div>

            </div>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row">
                <label>Num. Theaters</label>
                <input className="form-control col-1"
                value={this.state.numTheaters1}
                onChange={(event) => this.setState({numTheaters1: event.target.value})}
                />
                <div>--</div>
                <input className="form-control col-1"
                value={this.state.numTheaters2}
                onChange={(event) => this.setState({numTheaters2: event.target.value})}/>
                <label>Num. Employees</label>
                <input className="form-control col-1"
                value={this.state.numEmployees1}
                onChange={(event) => this.setState({numEmployees1: event.target.value})}/>
                <div>--</div>
                <input className="form-control col-1"
                value={this.state.numEmployees2} 
                onChange={(event) => this.setState({numEmployees2: event.target.value})}/>
              </div>
            </div>
            <div className="row">
              <button className="btn btn-primary col-3" onClick={this.handleFilter}>Filter</button>
              <div className="col-3"></div>
              <a className="btn btn-primary col-2" href="/auth/create-theater">Create Theater</a>
              <button className="btn btn-primary col-2" onClick={this.handleCompDetail}>Detail</button>
            </div>
            
            <div className="functionalities-table visitHistoryTableCard">
            <table className="table">
              <thead>
                <tr>
                  <th scope="col">Selected</th>
                  <th scope="col">Name</th>
                  <th scope="col">Num. Cities Covered</th>
                  <th scope="col">Num. Theaters</th>
                  <th scope="col">Num. Employees</th>
                </tr>
              </thead>
              <tbody>
                
                  {this.state.rowData.map( (row) => {
                    var index= this.state.rowData.indexOf(row)
                    return (
                      <tr key={this.state.rowData.indexOf(row)}>
                        <td><input type="radio" name="optradio" id={index} onClick={() => this.setState({companyIndex: index})}/></td>
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