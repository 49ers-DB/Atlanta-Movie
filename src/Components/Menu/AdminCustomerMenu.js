import React from 'react'

const AdminCustomerMenu = () => {

  return (
    <div className="card">
      <div className="card-header">
        <h2>Admin-Customer Functionalities</h2>
      </div>
      <div className="card-body">
        <div className="row">
          <a className="btn btn-primary" href="">Manage User</a>
          <a className="btn btn-primary" href="">Explore Movie</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Manage Company</a>
          <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Create Movie</a>
          <a className="btn btn-primary" href="">View History</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="/auth/visit-history">Visit History</a>
          <a className="btn btn-primary" href="">Back</a>
        </div>
      </div>
    </div>
  );
};

export default (AdminCustomerMenu);