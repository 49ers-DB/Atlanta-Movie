import axios from 'axios'

const BASE_URI = 'http://localhost:4433'


const client = axios.create({
  base_url: BASE_URI,
  json: true
});


class APIClient {
  constructor(accessToken) {
    this.accessToken = accessToken;
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
