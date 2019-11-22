import React, { Component } from "react";
import ErrorScreen from "../ErrorScreen.js"
import { UserMenu } from "./UserMenu.js";
import { CustomerMenu } from "./CustomerMenu.js";
import ManagerMenu from "./ManagerMenu.js";
import ManagerCustomerMenu from "./ManagerCustomerMenu.js";
import AdminMenu from "./AdminMenu.js";
import AdminCustomerMenu from "./AdminCustomerMenu.js";

export default class Menu extends Component {
  constructor(props) {
    super(props)
    this.state = {
      userType: 'u'
    }

    //api call here to get user type
    if (this.props.apiClient !== undefined && this.props.apiClient.accessToken) {
      console.log(this.props.apiClient)
      this.props.apiClient.example().then( data => {
        console.log("got api Request change me to get usertype and set state")
        this.setState({userType: 'user'})
      });
    }
    
  }

  render () {
    var menuBody = null
    if (this.props.apiClient === null) {
      menuBody = <ErrorScreen/>
    } else if (this.state.userType === 'customer') {
      menuBody = <CustomerMenu/>
    } else if (this.state.userType === 'manager') {
      menuBody = <ManagerMenu/>
    } else if (this.state.userType === 'manager-customer') {
      menuBody = <ManagerCustomerMenu/>
    } else if (this.state.userType === 'admin') {
      menuBody = <AdminMenu/>
    } else if (this.state.userType === 'admin-customer') {
      menuBody = <AdminCustomerMenu/>
    } else if (this.state.userType === 'user') {
      menuBody = <UserMenu/>
    } else {
      menuBody = <ErrorScreen/>
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