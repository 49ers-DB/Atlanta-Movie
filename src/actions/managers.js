import APIClient from "../apiClient"

const managers = () => {
    var managers = []
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      apiClient.perform("get", "/managers").then( resp => {
        resp['managers'].map( manager => {
          var name = manager['firstname'] + " " + manager['lastname']

          managers.push({value: name, label: name})
        })
        
      });
    }
    return managers;
  }


export default managers;