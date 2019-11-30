import React, { Component } from 'react'
import {Redirect} from 'react-router-dom'
import APIClient from "../../../apiClient"
import Select from 'react-select'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faSortAlphaUp,
  faSortAlphaDown
} from '@fortawesome/free-solid-svg-icons'

import "../Functionality.css"
import getCompanies from '../../../actions/companies'

export default class ManageCompany extends Component {
  constructor(props) {
    super(props)
    this.state = {
      redirect: false,
      rowData: [],
      selectedComName: null,
      numCitiesCov1: "",
      numCitiesCov2: "",
      numTheaters1: "",
      numTheaters2: "",
      numEmployees1: "",
      numEmployees2: "",
      companyIndex: null,
      sortBy: "comName",
      sortDirection: "DESC",
      reverseCompanyCol: false,
      reverseCityCoveredCol: false,
      reverseTheaterCol: false,
      reverseEmployeeCol: false,
    }
    this.handleFilter = this.handleFilter.bind(this)
    this.handleCompDetail = this.handleCompDetail.bind(this)
    this.renderRedirect = this.renderRedirect.bind(this)

    this.handleFilter(new Event(""))
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    console.log(this.state.reverseCompanyCol)
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      var requestBody = {
        i_comName: this.state.selectedComName,
        i_minCity: this.state.numCitiesCov1,
        i_maxCity: this.state.numCitiesCov2,
        i_minTheater: this.state.numTheaters1,
        i_maxTheater: this.state.numTheaters2,
        i_minEmployee: this.state.numEmployees1,
        i_maxEmployee: this.state.numEmployees2,
        i_sortBy: this.state.sortBy,
        i_sortDirection: this.state.sortDirection,
      }
      console.log(requestBody)
      
      apiClient.perform('post', '/manageCompany', requestBody)
      .then( resp => {
        this.setState({rowData: resp['data']},
        function() {
          console.log(this.state.rowData)
        })
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
      var comName = this.state.rowData[this.state.companyIndex]["Company"]
      return <Redirect to={'/Auth/Company-Detail/' + comName}/>
    }
  }

  handleComNameClick(revCom, comDirection) {
    this.setState({
      reverseCompanyCol: revCom,
      sortBy: "comName",
      sortDirection: comDirection
      }, () =>  {
      this.handleFilter(new Event(""))})
  }

  handleCityCoveredClick(revCityCov, cityCovDirection) {
    this.setState({
      reverseCityCoveredCol: revCityCov,
      sortBy: "numCityCover",
      sortDirection: cityCovDirection
      }, () =>  {
      this.handleFilter(new Event(""))})
  }

  handleTheaterClick(revTh, thDirection) {
    this.setState({
      reverseTheaterCol: revTh,
      sortBy: "numTheater",
      sortDirection: thDirection
      }, () =>  {
      this.handleFilter(new Event(""))})
  }

  handleEmployeeClick(revEm, emDirection) {
    this.setState({
      reverseEmployeeCol: revEm,
      sortBy: "numEmployee",
      sortDirection: emDirection
    }, () =>  {
      this.handleFilter(new Event(""))})
  }


  render () {
    var comNameIcon = faSortAlphaDown
    var revCom = this.state.reverseCompanyCol
    var comDirection = 'ASC'
    if (this.state.reverseCompanyCol) {
      comNameIcon = faSortAlphaUp
      comDirection = 'DESC'
    }
    var cityCovIcon = faSortAlphaDown
    var revCityCov = this.state.reverseCityCoveredCol
    var cityCovDirection = 'ASC'
    if (this.state.reverseCityCoveredCol) {
      cityCovIcon = faSortAlphaUp
      cityCovDirection = 'DESC'
    }
    var thIcon = faSortAlphaDown
    var revTh = this.state.reverseTheaterCol
    var thDirection = 'ASC'
    if (this.state.reverseTheaterCol) {
      thIcon = faSortAlphaUp
      thDirection = 'DESC'
    }
    var emIcon = faSortAlphaDown
    var revEm = this.state.reverseEmployeeCol
    var emDirection = 'ASC'
    if (this.state.reverseEmployeeCol) {
      emIcon = faSortAlphaUp
      emDirection = 'DESC'
    }
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
                  <th scope="col">Name <FontAwesomeIcon
                    icon={comNameIcon} 
                    onClick={() => {this.handleComNameClick(!revCom, comDirection)}}
                  />
                  </th>
                  <th scope="col">Num. Cities Covered<FontAwesomeIcon
                    icon={cityCovIcon} 
                    onClick={() => {this.handleCityCoveredClick(!revCityCov, cityCovDirection)}}
                  /></th>
                  <th scope="col">Num. Theaters<FontAwesomeIcon
                    icon={thIcon} 
                    onClick={() => {this.handleTheaterClick(!revTh, thDirection)}}
                  /></th>
                  <th scope="col">Num. Employees<FontAwesomeIcon
                    icon={emIcon} 
                    onClick={() => {this.handleEmployeeClick(!revEm, emDirection)}}
                  /></th>
                </tr>
              </thead>
              <tbody>
                
                  {this.state.rowData.map( (row) => {
                    var index= this.state.rowData.indexOf(row)
                    return (
                      <tr key={this.state.rowData.indexOf(row)}>
                        <td><input type="radio" name="optradio" id={index} onClick={() => this.setState({companyIndex: index})}/></td>
                        <td>{row["Company"]}</td>
                        <td>{row["City Count"]}</td>
                        <td>{row["Theater Count"]}</td>
                        <td>{row["Employee Count"]}</td>
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