import React, { Component } from 'react'
import ErrorScreen from '../ErrorScreen'
import { Route, Switch } from 'react-router-dom'
import ExploreTheater from './User/ExploreTheater';
import VisitHistory from './User/VisitHistory';
import ViewHistory from './Customer/ViewHistory';
import ExploreMovie from './Customer/ExploreMovie';
import TheaterOverview from './Manager/TheaterOverview';
import ScheduleMovie from './Manager/ScheduleMovie';
import CreateMovie from './Admin/CreateMovie';
import ManageCompany from './Admin/ManageCompany';
import ManageUser from './Admin/ManageUser';


export default class Auth extends Component {
  constructor(props) {
    super(props)
    this.state = {
      accessToken: localStorage.getItem("accessToken")
    }
    
  }

  render () {
    
    if (this.state.accessToken) {
      return (
        <Switch>
          <Route exact path="/Auth/Explore-Theater" component={ExploreTheater}/>
          <Route exact path="/Auth/Visit-History" component={VisitHistory}/>
          <Route exact path="/Auth/View-History" component={ViewHistory}/>
          <Route exact path="/Auth/Explore-Movie" component={ExploreMovie}/>
          <Route exact path="/Auth/Schedule-Movie" component={ScheduleMovie}/>
          <Route exact path="/Auth/Theater-Overview" component={TheaterOverview}/>
          <Route exact path="/Auth/Create-Movie" component={CreateMovie}/>
          <Route exact path="/Auth/Manage-Company" component={ManageCompany}/>
          <Route exact path="/Auth/Manage-User" component={ManageUser}/>
        </Switch>

      );

    } else {
      return (
        <div className="main">
          <Switch>
            <Route exact path="/Auth/Explore-Theater" component={ErrorScreen}/>
            <Route exact path="/Auth/" component={ErrorScreen}/>
          </Switch>
          
        </div>
      )
    }
  }

}