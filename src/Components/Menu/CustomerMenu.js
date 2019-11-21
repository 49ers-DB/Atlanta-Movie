import React, {Component} from "react"

export class CustomerMenu extends Component {


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
            <a className="btn btn-primary" href="">Explore Theater</a>
            <a className="btn btn-primary" href="">Visit Movie</a>
          </div>
          <div className="row">
            <a className="btn btn-primary" href="">Back</a>
          </div>
        </div>
      </div>
    )
  }
}