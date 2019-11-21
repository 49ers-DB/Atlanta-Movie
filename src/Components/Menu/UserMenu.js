import React, {Component} from "react"
import "./Menu.css"


export class UserMenu extends Component {


  render () {
    return (
      <div className="card">
        <h2 className="card-header">User Functionality</h2>
        <div className="card-body">
          <div className="row">
              <a className="btn btn-primary" href="/explore-theater">Explore Theater</a>
          </div>
          <div className="row">
                <a className="btn btn-primary" href="/visit-history">Visit History</a>
          </div>
          <div className="row">
                <a className="btn btn-primary" href="/">Back</a>
          </div>
        </div>
      </div>
    )
  }
}
