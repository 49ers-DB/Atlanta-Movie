import React, { Component } from 'react'
import Select from 'react-select'
import APIClient from "../../../apiClient"
import "../Functionality.css"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
  faSortAlphaUp,
  faSortAlphaDown
} from '@fortawesome/free-solid-svg-icons'
 

const statuses = [
  {value:"All", label:"All"},
  {value:"Approved", label:"Approved"},
  {value:"Pending", label:"Pending"},
  {value:"Declined", label:"Declined"}
]

export default class ManageUser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      username: "",
      rowData: [[],[],[],[],[],[]],
      i_status: null,
      reverseUsernameCol: true,
      reverseCreCardCountCol: true,
      reverseUserTypeCol: true,
      reverseStatusCol: true,
      userIndex: null,
      i_sortBy: "username",
      i_sortDirection: "desc"

    }

    this.handleFilter = this.handleFilter.bind(this)
    this.handleApprove = this.handleApprove.bind(this)
    this.handleDecline = this.handleDecline.bind(this)

    this.handleFilter(new Event(""))
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      var requestBody = JSON.parse(JSON.stringify(this.state))
      console.log(apiClient)
      if (requestBody.selectedStatus) {
        requestBody.selectedStatus = requestBody.selectedStatus['value']
      }
      
      apiClient.perform("post", "/filterUser", requestBody).then( resp => {
        console.log(resp)
        this.setState({rowData: resp['data']})
      })
      .catch( error => {
        window.alert(`Error talking to server: ${error.message}`)
      });



    }
  }

  handleApprove(event) {
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken && this.state.userIndex) {
      var apiClient = new APIClient(accessToken)
      
      apiClient.perform("post", "/approveUser", this.state).then( resp => {

      })
      .catch( error => {
        window.alert(`Error talking to server: ${error.message}`)
      });

    }
  }

  handleDecline(event) {
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken && this.state.userIndex) {
      var apiClient = new APIClient(accessToken)
      
      apiClient.perform("post", "/declineUser", this.state).then( resp => {

      })
      .catch( error => {
        window.alert(`Error talking to server: ${error.message}`)
      });

    }
  }


  render () {
    var usernameIcon = faSortAlphaUp
    var revUsername = this.state.reverseUsernameCol
    var usernameDirection = 'desc'
    if (this.state.reverseUsernameCol) {
      usernameIcon = faSortAlphaDown
      usernameDirection = 'asc'
    }
    var creditCardIcon = faSortAlphaUp
    var revCredCard = this.state.reverseCreCardCountCol
    var creditCardDirection = 'desc'
    if (this.state.reverseCreCardCountCol) {
      creditCardIcon = faSortAlphaDown
      creditCardDirection = 'asc'
    }
    var userTypeIcon = faSortAlphaUp
    var revUserType = this.state.reverseUserTypeCol
    var userTypeDirection = 'desc'
    if (this.state.reverseUserTypeCol) {
      userTypeIcon = faSortAlphaDown
      userTypeDirection = 'asc'
    }
    var statusIcon = faSortAlphaUp
    var revStatus = this.state.reverseStatusCol
    var statusDirection = 'desc'
    if (this.state.reverseStatusCol) {
      statusIcon = faSortAlphaDown
      statusDirection = 'asc'
    }
    return (
      <div className="main">
        <div className="card visitHistoryCard">
          <div className="card-header">
            <h2>Manage User</h2>
          </div>
          <div className="card-body">
            <div className="row form-group">
              <div className="form-inline col">
                <label className="col">Username</label>
                <input className="form-control col-4"
                 value={this.state.username}
                 onChange={(event) => this.setState({username: event.target.value})}/>
                <label className="col">Status</label>
                <Select className="functionalities-select col-4"
                  value={this.state.i_status}
                  options={statuses}
                  onChange={(status) => this.setState({selectedStatus: status})}
                />
              </div>
            </div>
            <div className="row">
                <button className="btn btn-primary col-2" onClick={this.handleFilter}>Filter</button>
                <div className="col-3"></div>
                <button className="btn btn-primary col-2" onClick={this.handleApprove}>Approve</button>
                <button className="btn btn-primary col-2" onClick={this.handleDecline}>Decline</button>
            </div>
          <div className="functionalities-table">
          <i className="fas fa-sort-alpha-up"></i>
          <table className="table">
            <thead>
              <tr>
                <th scope="col">
                  Selected
                </th>
                <th scope="col">Username  <FontAwesomeIcon
                  icon={usernameIcon} 
                  onClick={() => this.setState({
                    reverseUsernameCol: !revUsername,
                    i_sortBy: "username",
                    i_sortDirection: usernameDirection
                  })}
                  />
                </th>
                <th scope="col">Credit Card Count  <FontAwesomeIcon
                  icon={creditCardIcon}
                  onClick={() => this.setState({
                    reverseCreCardCountCol: !revCredCard,
                    i_sortBy: "creditCardCount",
                    i_sortDirection: creditCardDirection
                  })}
                  />
                </th>
                <th scope="col">User Type  <FontAwesomeIcon
                  icon={userTypeIcon}
                  onClick={() => this.setState({
                    reverseUserTypeCol: !revUserType,
                    i_sortBy: "userType",
                    i_sortDirection: userTypeDirection
                  })}
                  />
                </th>
                <th scope="col">Status  <FontAwesomeIcon
                  icon={statusIcon}
                  onClick={() => this.setState({
                    reverseStatusCol: !revStatus,
                    i_sortBy: "status",
                    i_sortDirection: statusDirection
                  })}
                  />
                </th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  var keyV = this.state.rowData.indexOf(row)
                  return (
                    <tr key={keyV}>
                      <td><input type="radio" name="radioclass" onClick={() => this.setState({userIndex: keyV})}/></td>
                      <td>{row.username}</td>
                      <td>{row.creditCardNum}</td>
                      <td>{row.userType}</td>
                      <td>{row.status}</td>
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