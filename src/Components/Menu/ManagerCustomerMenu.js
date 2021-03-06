import React from 'react'



const ManagerCustomerMenu = () => {
  function logout(){
    localStorage.setItem("accessToken", false)
    window.location.replace("/");
  };

  return (
    <div className="card">
      <div className="card-header">
        <h2>Manager-Customer Functionalities</h2>
      </div>
      <div className="card-body">
        <div className="row">
          <a className="btn btn-primary" href="/auth/theater-overview">Theater Overview</a>
          <a className="btn btn-primary" href="/auth/explore-movie">Explore Movie</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="/auth/schedule-movie">Schedule Movie</a>
          <a className="btn btn-primary" href="/auth/explore-theater">Explore Theater</a>
        </div>
        <div className="row">
          <a className="btn btn-primary" href="/auth/view-history">View History</a>
          <a className="btn btn-primary" href="/auth/visit-history">Visit History</a>
        </div>
        <div className="row">
          <div className="btn btn-primary" onClick={logout}>Back</div>
        </div>
      </div>
    </div>
  );
};

export default (ManagerCustomerMenu);