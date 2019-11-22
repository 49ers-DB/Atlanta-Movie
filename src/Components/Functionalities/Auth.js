import React, { Component } from 'react'
import ErrorScreen from '../ErrorScreen'
import { Route, Switch } from 'react-router-dom'
import ExploreTheater from './User/ExploreTheater';


export default class Auth extends Component {
  constructor(props) {
    super(props)
  }

  render () {
    
    if (this.props.apiClient) {
      return (
        <Switch>
          <Route exact path="/Auth/Explore-Theater" component={() => <ExploreTheater apiClient={this.props.apiClient}/>}/>
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