import React from 'react'

const ManagerCustomerMenu = () => {

  return (
    <div className="card">
      <div className="card-header">
        <h2>Manager-Customer Functionalities</h2>
      </div>
      <div className="card-body">
        <div className="row">
          <a className="btn btn-primary" href="">Theater Overview</a>
          <a className="btn btn-primary" href="">Explore Movie</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Schedule Movie</a>
          <a className="btn btn-primary" href="">Explore Theater</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">View History</a>
          <a className="btn btn-primary" href="">Visit History</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Back</a>
        </div>
      </div>
    </div>
  );
};

export default (ManagerCustomerMenu);