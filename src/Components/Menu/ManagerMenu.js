import React from 'react'

const ManagerMenu = () => {

  return (
    <div className="card">
      <div className="card-header">
        <h2>Manager Functionalities</h2>
      </div>
      <div className="card-body">
        <div className="row">
          <a className="btn btn-primary" href="">Theater Overview</a>
          <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Schedule Movie</a>
          <a className="btn btn-primary" href="/auth/visit-history">Visit History</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Back</a>
        </div>
      </div>
    </div>
  );
};

export default (ManagerMenu);