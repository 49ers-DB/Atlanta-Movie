import React, {Component} from "react"
import "./Menu.css"


export class UserMenu extends Component {
  logout(){
    localStorage.setItem("accessToken", false)
    window.location.replace("/");
  };


  render () {
    return (
      <div className="card">
        <h2 className="card-header">User Functionality</h2>
        <div className="card-body">
          <div className="row">
              <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
          </div>
          <div className="row">
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
