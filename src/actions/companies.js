import APIClient from "../apiClient"

const getCompanies = () => {
    var companies = [{value:"ALL", label:"ALL"}]
    var accessToken = localStorage.getItem("accessToken")
    
    if (accessToken) {
      var apiClient = new APIClient(accessToken)
      apiClient.getCompanies().then( resp => {
        for(var i = 0; i < resp.length; i++) {
          var companyName = resp[i].comName;
          companies[i + 1] = {value: companyName, label: companyName}
        }
      });
    
    }
    return companies;
  }


export default getCompanies;