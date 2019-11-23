import React from 'react'

const AdminMenu = () => {

  return (
    <div className="card">
      <div className="card-header">
        <h2>Admin Functionalities</h2>
      </div>
      <div className="card-body">
        <div className="row">
          <a className="btn btn-primary" href="">Manage User</a>
          <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Manage Company</a>
          <a className="btn btn-primary" href="">Visit History</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="">Create Movie</a>
          <a className="btn btn-primary" href="">Back</a>
        </div>
      </div>
    </div>
  );
};

export default (AdminMenu);