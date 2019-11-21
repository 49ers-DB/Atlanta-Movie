import React, { Component } from "react";
import ErrorScreen from "../ErrorScreen.js"
import { UserMenu } from "./UserMenu.js";
import { CustomerMenu } from "./CustomerMenu.js";
import apiClient from "../../App.js";




export default class Menu extends Component {
  constructor(props) {
    super(props)
    //api call here to get user type
    this.state = {
      userType: 'user'
    }
  }

  render () {
    var menuBody = null
    if (this.props.apiClient === null) {
      menuBody = <ErrorScreen/>
    }  if (this.state.userType === 'customer') {
      menuBody = <CustomerMenu/>
    } else if (this.state.userType === 'customer') {
      
    } else if (this.state.userType === 'manager') {

    } else if (this.state.userType === 'manager-customer') {

    } else if (this.state.userType === 'admin') {

    } else if (this.state.userType === 'admin-customer') {

    } else {
      menuBody = <UserMenu/>
    }
    return (
      <div className='main'>
          <div className='menu'>
              {menuBody}
          </div>
      </div>
    )
  }
}