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