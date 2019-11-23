import React, {Component} from "react"

export class CustomerMenu extends Component {
  logout(){
    localStorage.setItem("accessToken", false)
    window.location.replace("/");
  };


  render () {
    return (
      <div className="card">
        <div className="card-header">
          <h2>Customer Functionalities</h2>
        </div>
        <div className="card-body">
          <div className="row">
            <a className="btn btn-primary" href="">Explore Movie</a>
            <a className="btn btn-primary" href="">View History</a>
          </div>
          <div className="row">
            <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
            <a className="btn btn-primary" href="/auth/visit-history">Visit History</a>
          </div>
          <div className="row">
            <div className="btn btn-primary" onClick={this.logout()}>Back</div>
          </div>
        </div>
      </div>
    )
  }
}