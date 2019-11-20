import React, {Component} from "react";
import './NavBar.css'


export default class NavBar extends Component {
    render() {
        return(
        <nav className="navbar shadow p-1 mb-5 navbar-expand navbar-light bg-light" id="navBarMain">
            <a className="navbar-brand" href="/">Atlanta Movie</a> 
        </nav>
        )
    }
}