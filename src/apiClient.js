import axios from 'axios'

const BASE_URI = 'http://localhost:4433'


const client = axios.create({
  baseURL: BASE_URI,
  json: true
});


class APIClient {
  constructor(accessToken) {
    this.accessToken = accessToken;
  }

  //-----Register-----
  registerUser(userData) {
    return this.perform("post", "/userRegister", userData)
  }

  registerManager(userData) {
    return this.perform("post", "/managerRegister", userData)
  }

  registerCustomer(userData) {
    return this.perform("post", "/customerRegister", userData)
  }

  registerManagerCustomer(userData) {
    return this.perform("post", "/managerCustomerRegister", userData)
  }

  getCompanies() {
    return this.perform("get", "/getCompanies")
  }
  

  //-------User_Type-------
  getUser(userData) {
    return this.perform("get", "/user", userData)
  }

  //---------Data_Getters-----------

  getTheaters(companyName) {
    return this.perform('get', `/theaters/${companyName}`);
  }

  getCompanies() {
    return this.perform('get', '/getCompanies');
  }

  

  createTheater(theater) {
    return this.perform('post', '/kudos', theater);
  }

  example() {
    return this.perform('get', '/example/12');
  }


  async perform (method, resource, data) {
    return client({
      method,
      url: resource,
      data,
      headers: {
        Authorization: `Bearer ${this.accessToken}`
      }
    }).then(resp => {
      return resp.data ? resp.data : [];
    })
  }

}

export default (APIClient);