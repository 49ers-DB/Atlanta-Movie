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
  {value:"ALL", label:"ALL"},
  {value:"Approved", label:"Approved"},
  {value:"Pending", label:"Pending"},
  {value:"Declined", label:"Declined"}
]

var oldRow = {
  username:""
}

export default class ManageUser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      username: "",
      rowData: [[],[],[],[],[],[]],
      i_status: null,
      reverseUsernameCol: false,
      reverseCreCardCountCol: false,
      reverseUserTypeCol: false,
      reverseStatusCol: false,
      userIndex: null,
      i_sortBy: "username",
      i_sortDirection: "desc"

    }

    this.handleFilter = this.handleFilter.bind(this)
    this.handleApprove = this.handleApprove.bind(this)
    this.handleDecline = this.handleDecline.bind(this)
    this.handleClick = this.handleClick.bind(this)
    this.handleRowChange  = this.handleRowChange.bind(this)

    this.handleFilter(new Event(""))
  }

  handleClick() {
    
    this.handleFilter(new Event(""))

  }

  handleRowChange() {
    let i = this.state.userIndex

    if (this.state.userIndex >= 0) {
      var newIndex = -1
      this.state.rowData.map( (rowD, ind) => {
        if (oldRow["username"] === rowD["username"]) {
          newIndex = ind
        }
      });
      this.setState({userIndex: newIndex});
    }
  }

  handleFilter(event) {
    event.preventDefault()
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      var requestBody = JSON.parse(JSON.stringify(this.state))
      
      if (requestBody.i_status) {
        requestBody.i_status = requestBody.i_status['value']
      }

      let i = this.state.userIndex
      if (this.state.userIndex && this.state.userIndex >= 0) {
        oldRow = JSON.parse(JSON.stringify(this.state.rowData[i]));
      }
      
      console.log(requestBody)

      apiClient.perform("post", "/filterUser", requestBody).then( resp => {
        this.setState({rowData: resp['data']}, this.handleRowChange)
      })
      .catch( error => {
        window.alert(`Error talking to server: ${error.message}`)
      });



    }
  }

  handleApprove(event) {
    var accessToken = localStorage.getItem("accessToken")
    
    console.log(this.state)
    if (accessToken && this.state.userIndex >= 0 && this.state.rowData) {
      var apiClient = new APIClient(accessToken)

      var username  = this.state.rowData[this.state.userIndex]['username']
      var requestBody = {
        i_username: username
      }
      console.log(requestBody)
      apiClient.perform("post", "/approveUser", requestBody ).then( resp => {
        window.alert("Approved User")
        this.handleFilter(new Event(""))
      })
      .catch( error => {
        window.alert(`Error talking to server: ${error.message}`)
      });

    } else {
      window.alert("Please select a User")
    }
  }

  handleDecline(event) {
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken && this.state.userIndex >= 0 && this.state.rowData) {
      var apiClient = new APIClient(accessToken)

      var username  = this.state.rowData[this.state.userIndex]['username']
      var requestBody = {
        i_username: username
      }
      
      apiClient.perform("post", "/declineUser", requestBody).then( resp => {
        window.alert("Declined User")
        this.handleFilter(new Event(""))

      })
      .catch( error => {
        window.alert(`Error talking to server: ${error.message}`)
      });

    } else {
      window.alert("Please select a User")
    }
  }

  handleUsernameClick(revUsername, usernameDirection) {
    console.log(usernameDirection)
    this.setState({
      reverseUsernameCol: !revUsername,
      i_sortBy: "username",
      i_sortDirection: usernameDirection
      }, () => 
      {this.handleClick()})
    
  }

  handleCreditCardClick(revCredCard, creditCardDirection) {
    this.setState({
      reverseCreCardCountCol: !revCredCard,
      i_sortBy: "creditCardCount",
      i_sortDirection: creditCardDirection
      }, () => 
      {this.handleClick()})
  }

  handleUserTypeClick(revUserType, userTypeDirection) {
    this.setState({
      reverseUserTypeCol: !revUserType,
      i_sortBy: "userType",
      i_sortDirection: userTypeDirection
      }, () => 
      {this.handleClick()})
    
  }

  handleStatusClick(revStatus, statusDirection) {
    this.setState({
      reverseStatusCol: !revStatus,
      i_sortBy: "status",
      i_sortDirection: statusDirection
      }, () => 
      {this.handleClick()})
    
  }


  render () {
    var usernameIcon = faSortAlphaDown
    var revUsername = this.state.reverseUsernameCol
    var usernameDirection = 'asc'
    if (this.state.reverseUsernameCol) {
      usernameIcon = faSortAlphaUp
      usernameDirection = 'desc'
    }
    var creditCardIcon = faSortAlphaDown
    var revCredCard = this.state.reverseCreCardCountCol
    var creditCardDirection = 'asc'
    if (this.state.reverseCreCardCountCol) {
      creditCardIcon = faSortAlphaUp
      creditCardDirection = 'desc'
    }
    var userTypeIcon = faSortAlphaDown
    var revUserType = this.state.reverseUserTypeCol
    var userTypeDirection = 'asc'
    if (this.state.reverseUserTypeCol) {
      userTypeIcon = faSortAlphaUp
      userTypeDirection = 'desc'
    }
    var statusIcon = faSortAlphaDown
    var revStatus = this.state.reverseStatusCol
    var statusDirection = 'asc'
    if (this.state.reverseStatusCol) {
      statusIcon = faSortAlphaUp
      statusDirection = 'desc'
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
                  onChange={(status) => this.setState({i_status: status})}
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
                  onClick={() => {this.handleUsernameClick(revUsername, usernameDirection)}}
                  />
                </th>
                <th scope="col">Credit Card Count  <FontAwesomeIcon
                  icon={creditCardIcon}
                  onClick={() => {this.handleCreditCardClick(revCredCard, creditCardDirection)}}
                  />
                </th>
                <th scope="col">User Type  <FontAwesomeIcon
                  icon={userTypeIcon}
                  onClick={() => {this.handleUserTypeClick(revUserType, userTypeDirection)}}
                  />
                </th>
                <th scope="col">Status  <FontAwesomeIcon
                  icon={statusIcon}
                  onClick={() => {this.handleStatusClick(revStatus, statusDirection)}}
                  />
                </th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  var keyV = this.state.rowData.indexOf(row)
                  var i = -1
                  if (this.state.userIndex || this.state.userIndex === 0) {
                    i = this.state.userIndex
                  }
                  
                  return (
                    <tr key={keyV}>
                      <td><input type="radio" name="radioclass"
                       checked={keyV===i}
                       onChange={event => {}}
                       onClick={() => this.setState({userIndex: keyV})}/></td>
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