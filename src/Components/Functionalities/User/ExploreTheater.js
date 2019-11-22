import React, { Component } from 'react'
import DatePicker from "react-datepicker";
import "../Functionality.css"

import "react-datepicker/dist/react-datepicker.css";

export default class ExploreTheater extends Component {
  constructor(props) {
    super(props)
    this.state = {
      rowData: [
        ["","fdasfa",""],
        ["","2",""]
      ],
      theaters: [],
      companies: [],
      
      visitDate: new Date()
    }
  }

  handleFilter(event) {
    event.preventDefault()
  }

  handleLogVisit(event) {
    event.preventDefault()
  }

  handleChange(event) {
    
  }


  render () {
    return (
      <div className="main">
        <div className="card registrationCard">
          <div className="card-header">
            <h2>Explore Theater</h2>
          </div>

          <form>
            <div className="row">
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">Theater Name</label>
                <select className="form-control functionalities" id="theaterName"/>
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="comName">Company Name</label>
                <select className="form-control functionalities" id="comName"/>
              </div>  
            </div>
            <div className="row">
            <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="theaterName">City</label>
                <input className="form-control functionalities" id="city"/>
              </div>
              <div className="form-group form-inline functionalities-form-row col">
                <label htmlFor="comName">State</label>
                <select className="form-control functionalities" id="state"/>
              </div>  
            </div>
            <div className="row">
              <button className="btn btn-primary" onClick={this.handleFilter}>Filter</button>
            </div>
          </form>
          <div className="functionalities-table">
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Theater</th>
                <th scope="col">Address</th>
                <th scope="col">Company</th>
              </tr>
            </thead>
            <tbody>
              
                {this.state.rowData.map( (row) => {
                  return (
                    <tr key={this.state.rowData.indexOf(row)}>
                      <td>{row[0]}</td>
                      <td>{row[1]}</td>
                      <td>{row[2]}</td>
                    </tr>
                    
                  );
                })}
    
            </tbody>
          </table>
          </div>
          <div className="row">
            <div className="col-3">
              <a className="btn btn-primary" href="/">Back</a>
            </div>
            <div className="col functionalities-form-row">
                <label>Visit Date</label>
                <DatePicker className="form-control"
                  selected={this.state.visitDate}
                  onChange={this.handleChange}
                />
            </div>
            <div className="col-3">
              <button className="btn btn-primary" onClick={this.handleLogVisit}>Log Visit</button>
            </div>
              
              
            
          </div>
          

        </div>
          
      </div>
    )
  }
}
