import React, { Component } from 'react'
import ErrorScreen from '../ErrorScreen'
import { Route, Switch } from 'react-router-dom'
import ExploreTheater from './User/ExploreTheater';
import VisitHistory from './User/VisitHistory';
import ViewHistory from './Customer/ViewHistory';


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
          <Route exact path="/Auth/Explore-Theater" component={() => <ExploreTheater apiClient={this.props.apiClient}/>}/>
          <Route exact path="/Auth/Visit-History" component={() => <VisitHistory apiClient={this.props.apiClient}/>}/>
          <Route exact path="/Auth/View-History" component={() => <ViewHistory apiClient={this.props.apiClient}/>}/>
        </Switch>

      );

    } else {
      return (
        <div className="main">
          <Switch>
            <Route path="/Auth/Explore-Theater" component={ErrorScreen}/>
            <Route path="/Auth/" component={ErrorScreen}/>
          </Switch>
          
        </div>
      )
    }
  }

}