import React from 'react'

const AdminCustomerMenu = () => {
  function logout(){
    localStorage.setItem("accessToken", false)
    window.location.replace("/");
  };
  return (
    <div className="card">
      <div className="card-header">
        <h2>Admin-Customer Functionalities</h2>
      </div>
      <div className="card-body">
        <div className="row">
          <a className="btn btn-primary" href="/auth/manage-user">Manage User</a>
          <a className="btn btn-primary" href="/auth/explore-movie">Explore Movie</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="/auth/manage-company">Manage Company</a>
          <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="/auth/create-movie">Create Movie</a>
          <a className="btn btn-primary" href="/auth/view-history">View History</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="/auth/visit-history">Visit History</a>
          <div className="btn btn-primary" onClick={logout}>Back</div>
        </div>
      </div>
    </div>
  );
};

export default (AdminCustomerMenu);