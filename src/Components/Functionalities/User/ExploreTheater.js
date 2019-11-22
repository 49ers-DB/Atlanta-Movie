import React, { Component } from 'react'
import "../Functionality.css"

export default class ExploreTheater extends Component {
  constructor(props) {
    super(props)
  }


  render () {
    return (
      <div className="main">
        <div className="card">
          <div className="card-header">
            <h2>Explore Theater</h2>
          </div>
          <form>
            <div className="row ">
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">Theater Name</label>
                <select className="form-control" id="theaterName"/>
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="comName">Company Name</label>
                <select className="form-control" id="comName"/>
              </div>  
            </div>
            <div className="row">
            <div className="form-group form-inline">
                <label htmlFor="theaterName">City</label>
                <input className="form-control" id="city"/>
              </div>
              <div className="form-group form-inline">
                <label htmlFor="comName">State</label>
                <select className="form-control" id="state"/>
              </div>  
            </div>
          </form>
        </div>
          
      </div>
    )
  }
}
