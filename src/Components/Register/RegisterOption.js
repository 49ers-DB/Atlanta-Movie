import React, {Component} from "react";
import './RegisterOption.css'


export default class Login extends Component {
    
    render() {
        return(
            <div className="main">
                <div className="card loginCard">
                    <h2 className="card-header">Register Navigation</h2>
                    <div className="card-body">
                        <div className="row">
                        <a className="btn btn-primary registerOptions" href="/User-Registration">
                            User Only
                        </a>
                        </div>
                        <div className="row">
                        <a className="btn btn-primary registerOptions" href="/Customer-Registration">
                            Customer Only
                        </a>
                        </div>
                        <div className="row">
                        <a className="btn btn-primary registerOptions" href="/Manager-Registration">
                            Manager Only
                        </a>
                        </div>
                        <div className="row">
                        <a className="btn btn-primary registerOptions" href="/Manager-Customer-Registration">
                            Manager-Customer
                        </a>
                        </div>
                        <div className="row">
                        <a className="btn btn-primary registerOptions" href="/">
                            Back
                        </a>
                        </div>
                        
                        
                        
                        
                        
                    </div>
                </div>
            </div>
        )
    }
}