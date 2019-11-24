import React, { Component } from "react";


export default class ErrorScreen extends Component {
  componentDidMount() {
    localStorage.setItem("accessToken", false)
  }
  render () {
    return (
      <h1>Unauthorized Access</h1>
    )
  }
}