import React, { Component } from "react";
import { UserMenu } from "./UserMenu";
import { CustomerMenu } from "./CustomerMenu";



export default class Menu extends Component {
  constructor(props) {
    super(props)
    this.state = {
      userType: 'user'
    }
  }

  render () {
    var menuBody
    if (this.state.userType === 'customer') {
      menuBody = new CustomerMenu()
    } else if (this.state.userType === 'customer') {

    } else if (this.state.userType === 'manager') {

    } else if (this.state.userType === 'manager-customer') {

    } else if (this.state.userType === 'admin') {

    } else if (this.state.userType === 'admin-customer') {

    } else {
      menuBody = new UserMenu()
    }
    return (
    <div class='menu'>
        menuBody
    </div>
    )
  }
}